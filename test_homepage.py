# pylint: disable=redefined-outer-name

from playwright.sync_api import Page
import pytest
import allure

from shared.utils import (
    allure_annotation_fabric,
)
from pages.home import HomePage

EXPECTED_CAROUSEL_CHANGED_TIME = 6_000
EXPECTED_ADDED_2CART_PRODUCT = "MacBook"

allure_annotation = allure_annotation_fabric("Test eshop home page")


@pytest.fixture
def homepage(page: Page, eshop_url):
    homepage = HomePage(page, eshop_url)
    homepage.open()
    return homepage


@allure_annotation(
    "Carousel is playing",
    "Check that after few seconds one picture changes to another",
)
@allure.tag("homepage-ui", "carousel")
def test_carousel_playing(homepage):
    with allure.step("Remove the cursor from the carousel, so it won`t paused"):
        homepage.page.mouse.move(0, 0)

    def get_act_img_src():
        carousel = homepage.get_carousel()
        return carousel.locator(
            ".carousel-item.active img"
        ).first.get_attribute("src")

    with allure.step("Take a screenshot of the carousel slide"):
        slide_before = get_act_img_src()
        allure.attach(
            homepage.page.screenshot(full_page=False),
            name="slide_before",
            attachment_type=allure.attachment_type.PNG,
        )
    with allure.step(
        f"Take another screenshot after {EXPECTED_CAROUSEL_CHANGED_TIME/1_000}s"
    ):
        homepage.page.wait_for_timeout(EXPECTED_CAROUSEL_CHANGED_TIME)
        slide_after = get_act_img_src()
        allure.attach(
            homepage.page.screenshot(full_page=False),
            name="slide_after",
            attachment_type=allure.attachment_type.PNG,
        )
    assert slide_before != slide_after, "Carousel isn`t playing"


@allure_annotation(
    "Add product to cart",
    (
        "This test verifies that after click on cart button "
        "under the product it appears in cart widget"
    ),
)
@allure.tag("homepage-ui", "catalog-ui")
def test_add_product_2cart(homepage):
    homepage.add_product_2cart(EXPECTED_ADDED_2CART_PRODUCT)
    notification = homepage.get_notification()
    assert EXPECTED_ADDED_2CART_PRODUCT in notification.inner_text()
