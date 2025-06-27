import pytest
import allure
from playwright.sync_api import Page

from shared.utils import (
    allure_annotation_fabric,
)


ENTITY_NAME = "product"
allure_annotation = allure_annotation_fabric(f"Test {ENTITY_NAME} entity")


@pytest.fixture(scope="session")
@allure.title("Eshop base URL")
def base_url():
    return "http://localhost:8081"


@allure_annotation("Check homepage is loaded")
@allure.tag("Public UI")
def test_homepage_loads(page: Page, base_url):
    with allure.step("Navigate to homepage"):
        page.goto(base_url)
    assert "Your Store" in page.title()


@allure_annotation("Check MacBook product is found")
@allure.tag("Public UI")
def test_product_search(page: Page, base_url):
    with allure.step("Navigate to homepage"):
        page.goto(base_url)
    with allure.step("Input MacBook in search field"):
        search_input = page.locator('input[name="search"]')
        search_input.fill("MacBook")
    with allure.step("Press Enter for search"):
        search_input.press("Enter")
    assert page.locator("h1").inner_text() == "Search - MacBook"


@allure_annotation("Check MacBook product page is loaded")
@allure.tag("Public UI")
def test_product_page_opens(page: Page, base_url):
    with allure.step("Navigate to homepage"):
        page.goto(base_url)
    with allure.step("Input MacBook in search field"):
        page.locator('input[name="search"]').fill("MacBook")
    with allure.step("Press Enter for search"):
        page.locator('input[name="search"]').press("Enter")
    with allure.step("Click on the first found MacBook product"):
        page.locator("a:has-text('MacBook')").first.click()
    assert "MacBook" in page.locator("h1").inner_text()


# def test_add_product_to_cart(page):
#     page.goto("http://localhost:8081")
#     page.locator('input[name="search"]').fill("MacBook")
#     page.locator('input[name="search"]').press("Enter")
#     page.locator("a:has-text('MacBook')").first.click()
#     page.locator("#header-cart button").click()
#     page.locator("#header-cart .dropdown-menu a[href*='route=checkout/cart']").click()
#     assert "MacBook" in page.locator(".table-responsive").inner_text()


# def test_cart_link_navigates(page):
#     page.goto("http://localhost:8081")
#     page.locator("#cart-total").click()
#     page.locator("strong:has-text('View Cart')").click()
#     assert "Shopping Cart" in page.locator("h1").inner_text()


# def test_admin_login(page):
#     page.goto("http://localhost:8081/administrator")
#     page.locator('input[name="username"]').fill("user")
#     page.locator('input[name="password"]').fill("bitnami")
#     page.locator("button[type='submit']").click()
#     assert "Dashboard" in page.locator("h1").inner_text()


# def test_admin_open_orders(page):
#     page.goto("http://localhost:8081/administrator")
#     page.locator('input[name="username"]').fill("user")
#     page.locator('input[name="password"]').fill("bitnami")
#     page.locator("button[type='submit']").click()
#     page.locator("#menu-sale").click()
#     page.locator("a:has-text('Orders')").click()
#     assert "Order List" in page.locator("h1").inner_text()


# def test_admin_open_customers(page):
#     page.goto("http://localhost:8081/administrator")
#     page.locator('input[name="username"]').fill("user")
#     page.locator('input[name="password"]').fill("bitnami")
#     page.locator("button[type='submit']").click()
#     page.locator("#menu-customer").click()
#     page.locator("a:has-text('Customers')").click()
#     assert "Customer List" in page.locator("h1").inner_text()


# def test_admin_open_add_product_form(page):
#     page.goto("http://localhost:8081/administrator")
#     page.locator('input[name="username"]').fill("user")
#     page.locator('input[name="password"]').fill("bitnami")
#     page.locator("button[type='submit']").click()
#     page.locator("#menu-catalog").click()
#     page.locator("a:has-text('Products')").click()
#     page.locator("a[data-original-title='Add New']").click()
#     assert "General" in page.locator("ul.nav-tabs").inner_text()


# def test_admin_fill_product_name(page):
#     page.goto("http://localhost:8081/administrator")
#     page.locator('input[name="username"]').fill("user")
#     page.locator('input[name="password"]').fill("bitnami")
#     page.locator("button[type='submit']").click()
#     page.locator("#menu-catalog").click()
#     page.locator("a:has-text('Products')").click()
#     page.locator("a[data-original-title='Add New']").click()
#     page.locator('input[name="product_description[1][name]"]').fill("Test Product")
#     assert (
#         page.locator('input[name="product_description[1][name]"]').input_value()
#         == "Test Product"
#     )
