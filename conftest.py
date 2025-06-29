import os
import sys
import platform
import importlib.metadata
import subprocess
import pytest

from shared.constants import TEST_SUIT_NAME, ESHOP_BASE_URL
from shared.utils import wait_for_service


ALLURE_RESULT_DIR = "allure_results"
ALLURE_ENV_FILE = f"{ALLURE_RESULT_DIR}/environment.properties"
ESHOP_URL = f"http://{ESHOP_BASE_URL}"


def pytest_addoption(parser):
    parser.addoption(
        "--keep-docker",
        action="store_true",
        help="Don't stop Docker after tests",
    )


@pytest.fixture(scope="session")
def eshop_url():
    return ESHOP_URL


@pytest.fixture(scope="session")
def browser_context_args():
    """Playwright browser setups"""

    return {
        "viewport": None,  # fullscreen mode
        "ignore_https_errors": True,
    }


@pytest.fixture(scope="session", autouse=True)
def ensure_docker_up(request):
    """Starts docker before testing and stops after"""

    try:
        subprocess.run(["docker", "compose", "up", "-d"], check=True)
        wait_for_service(ESHOP_URL)
        yield
        if not request.config.getoption("--keep-docker"):
            subprocess.run(["docker", "compose", "down"], check=True)
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Docker Compose failed to start:\n{e}")


@pytest.fixture(scope="session", autouse=True)
def test_environment():
    """Captures environment details for the Allure report."""

    def get_version(package):
        try:
            return importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            return "Not Installed"

    os.makedirs(ALLURE_RESULT_DIR, exist_ok=True)
    allure_env_data = {
        r"Test\ object": f"{TEST_SUIT_NAME} on http://{ESHOP_BASE_URL}",
        "OS": f"{platform.system()} {platform.release()} ({platform.architecture()[0]})",
        "Python": sys.version.split()[0],
        "pytest": pytest.__version__,
        "pytest-playwright": get_version("pytest-playwright"),
        "allure-pytest": get_version("allure-pytest"),
    }

    with open(ALLURE_ENV_FILE, "w", encoding="utf-8") as f:
        for key, value in allure_env_data.items():
            f.write(f"{key}={value}\n")
