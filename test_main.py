import pytest
from playwright.sync_api import Page

BASE_URL = "http://localhost:8081"


def test_homepage_loads(page: Page):
    page.goto(BASE_URL)
    assert "Your Store" in page.title()


def test_product_search(page: Page):
    page.goto(BASE_URL)
    search_input = page.locator('input[name="search"]')
    search_input.fill("MacBook")
    search_input.press("Enter")
    assert page.locator("h1").inner_text() == "Search - MacBook"


def test_product_page_opens(page):
    page.goto("http://localhost:8081")
    page.locator('input[name="search"]').fill("MacBook")
    page.locator('input[name="search"]').press("Enter")
    page.locator("a:has-text('MacBook')").first.click()
    assert "MacBook" in page.locator("h1").inner_text()


def test_add_product_to_cart(page):
    page.goto("http://localhost:8081")
    page.locator('input[name="search"]').fill("MacBook")
    page.locator('input[name="search"]').press("Enter")
    page.locator("a:has-text('MacBook')").first.click()
    page.locator("#header-cart button").click()
    page.locator("#header-cart .dropdown-menu a[href*='route=checkout/cart']").click()
    assert "MacBook" in page.locator(".table-responsive").inner_text()


def test_cart_link_navigates(page):
    page.goto("http://localhost:8081")
    page.locator("#cart-total").click()
    page.locator("strong:has-text('View Cart')").click()
    assert "Shopping Cart" in page.locator("h1").inner_text()


def test_admin_login(page):
    page.goto("http://localhost:8081/administrator")
    page.locator('input[name="username"]').fill("user")
    page.locator('input[name="password"]').fill("bitnami")
    page.locator("button[type='submit']").click()
    assert "Dashboard" in page.locator("h1").inner_text()


def test_admin_open_orders(page):
    page.goto("http://localhost:8081/administrator")
    page.locator('input[name="username"]').fill("user")
    page.locator('input[name="password"]').fill("bitnami")
    page.locator("button[type='submit']").click()
    page.locator("#menu-sale").click()
    page.locator("a:has-text('Orders')").click()
    assert "Order List" in page.locator("h1").inner_text()


def test_admin_open_customers(page):
    page.goto("http://localhost:8081/administrator")
    page.locator('input[name="username"]').fill("user")
    page.locator('input[name="password"]').fill("bitnami")
    page.locator("button[type='submit']").click()
    page.locator("#menu-customer").click()
    page.locator("a:has-text('Customers')").click()
    assert "Customer List" in page.locator("h1").inner_text()


def test_admin_open_add_product_form(page):
    page.goto("http://localhost:8081/administrator")
    page.locator('input[name="username"]').fill("user")
    page.locator('input[name="password"]').fill("bitnami")
    page.locator("button[type='submit']").click()
    page.locator("#menu-catalog").click()
    page.locator("a:has-text('Products')").click()
    page.locator("a[data-original-title='Add New']").click()
    assert "General" in page.locator("ul.nav-tabs").inner_text()


def test_admin_fill_product_name(page):
    page.goto("http://localhost:8081/administrator")
    page.locator('input[name="username"]').fill("user")
    page.locator('input[name="password"]').fill("bitnami")
    page.locator("button[type='submit']").click()
    page.locator("#menu-catalog").click()
    page.locator("a:has-text('Products')").click()
    page.locator("a[data-original-title='Add New']").click()
    page.locator('input[name="product_description[1][name]"]').fill("Test Product")
    assert (
        page.locator('input[name="product_description[1][name]"]').input_value()
        == "Test Product"
    )
