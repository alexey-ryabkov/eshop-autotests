# pylint: disable=redefined-outer-name

from playwright.sync_api import Page
import pytest
import allure

from shared.utils import (
    allure_annotation_fabric,
)
from shared.assert_helper import assert_page_title_is
from pages.home import HomePage


CART_PRODUCT = "MacBook"
EXPECTED_CART_TITLE = "Shopping Cart"
EXPECTED_PRODUCT_QUANTITY = 5

allure_annotation = allure_annotation_fabric("Test eshop cart page")


@pytest.fixture
def cart_page(page: Page, eshop_url):
    homepage = HomePage(page, eshop_url)
    homepage.open()
    homepage.add_product_2cart(CART_PRODUCT)
    cart_page = homepage.go2cart()
    return cart_page


@allure_annotation(
    f"Open cart with added {CART_PRODUCT} product",
    "Check that the cart page contain the added product from homepage",
)
@allure.tag("cart-ui", "catalog-ui", "layout-ui")
def test_cart_contents(cart_page):
    assert cart_page.get_cart_item(CART_PRODUCT).is_visible()
    assert_page_title_is(EXPECTED_CART_TITLE, cart_page.page)


@allure_annotation(
    "Change product quantity",
    (
        "Check if we can change {CART_PRODUCT} product quantity ",
        "and this affects the cart total",
    ),
)
@allure.tag("cart-ui")
def test_change_quantity(cart_page):
    price_before = cart_page.get_cart_item_price(CART_PRODUCT)
    cart_page.change_quantity(CART_PRODUCT, EXPECTED_PRODUCT_QUANTITY)
    # price_after = cart_page.get_cart_item_price(CART_PRODUCT)
    price_after = cart_page.get_cart_total()
    assert (
        price_after == price_before * EXPECTED_PRODUCT_QUANTITY
    ), f"{CART_PRODUCT} price after change quantity is incorrect"


@allure_annotation(
    "Clear the cart",
    "Check that the cart can be cleared and becomes empty",
)
@allure.tag("cart-ui")
def test_clearing_cart(cart_page):
    cart_page.clear()
    assert not cart_page.get_cart_item(CART_PRODUCT).is_visible()
