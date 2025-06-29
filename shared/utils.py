import time
from functools import wraps
import allure
import requests

from .constants import TEST_SUIT_NAME


ALLURE_SUIT_TITLE = f"{TEST_SUIT_NAME} Tests"


def wait_for_service(url: str, timeout: int = 30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError(f"Timeout waiting for service at {url}")


def allure_annotation_fabric(feature: str, suite: str = ALLURE_SUIT_TITLE):
    """Decorators fabric for allure annotations"""

    def wrapper(title: str, description: str = None, story: str = None):
        return allure_annotation(suite, feature, title, description, story)

    return wrapper


def allure_annotation(
    suite: str,
    feature: str,
    title: str,
    description: str = None,
    story: str = None,
):
    """Decorator for allure annotations"""

    def decorator(test_func):
        decorated = allure.suite(suite)(test_func)
        decorated = allure.feature(feature)(decorated)
        decorated = allure.title(title)(decorated)
        if description:
            decorated = allure.description(description)(decorated)
        if story:
            decorated = allure.story(story)(decorated)

        @wraps(decorated)
        def wrapper(*args, **kwargs):
            return decorated(*args, **kwargs)

        return wrapper

    return decorator
