# pylint: disable=redefined-outer-name

from playwright.sync_api import Page
import pytest
import allure

from shared.utils import (
    allure_annotation_fabric,
)
from shared.assert_helper import assert_page_title_is
from pages.home import HomePage

EXPECTED_HOMEPAGE_TITLE = "Your Store"
EXPECTED_PHONE_NUMBER = "123456789"
EXPECTED_CURRENCY_NAME = "EUR"
EXPECTED_CURRENCY_SIGN = "€"

allure_annotation = allure_annotation_fabric("Test eshop common func")


@pytest.fixture
def homepage(page: Page, eshop_url):
    homepage = HomePage(page, eshop_url)
    homepage.open()
    return homepage


@allure_annotation(
    "Open the eshop",
    "Check that the eshop is accessible by opening the homepage",
)
@allure.tag("common")
def test_eshop_accessible(homepage):
    assert_page_title_is(EXPECTED_HOMEPAGE_TITLE, homepage.page)


@allure_annotation(
    "Phone number actuality",
    "Check if the phone number is actual",
)
@allure.tag("layout-ui")
def test_eshop_phone(homepage):
    assert (
        EXPECTED_PHONE_NUMBER
        in homepage.get_top_nav_links()
        .locator(".list-inline-item")
        .first.inner_text()
    )


@allure_annotation(
    "Change currency",
    (
        "This test verifies that after currency changed, "
        "its sign will appear in the cart widget button label"
    ),
)
@allure.tag("layout-ui", "currency")
def test_change_currency(homepage):
    homepage.change_currency(EXPECTED_CURRENCY_NAME)
    assert EXPECTED_CURRENCY_SIGN in homepage.get_cart_button().inner_text()
