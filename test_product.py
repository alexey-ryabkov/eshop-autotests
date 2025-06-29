# pylint: disable=redefined-outer-name

from playwright.sync_api import Page
import pytest
import allure

from shared.utils import (
    allure_annotation_fabric,
)
from shared.assert_helper import assert_page_title_is
from pages.product import ProductPage

PRODUCT_2TEST = "MacBook"
EXPECTED_PRODUCT_PAGE_TITLE = PRODUCT_2TEST

allure_annotation = allure_annotation_fabric("Test eshop product page")


@pytest.fixture
def product_page(page: Page, eshop_url):
    product_page = ProductPage(page, eshop_url)
    product_page.open(PRODUCT_2TEST)
    return product_page


@allure_annotation(
    f"Open {PRODUCT_2TEST} product page",
    "Check that the product page is available through the eshop search input",
)
@allure.tag("layout-ui", "search")
def test_product_accessible(product_page):
    assert_page_title_is(EXPECTED_PRODUCT_PAGE_TITLE, product_page.page)


@allure_annotation(
    "Check product gallery is opening",
)
@allure.tag("product-ui")
def test_gallery(product_page):
    product_page.open_gallery()
    gallery = product_page.get_gallery()
    gallery.wait_for(state="attached")
    gallery.wait_for(state="visible")
    assert gallery.locator(".mfp-img").is_visible()
