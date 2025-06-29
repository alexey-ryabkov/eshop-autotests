from playwright.sync_api import Page
from pages.search_page import SearchPage
from pages.cart_page import CartPage


class BasePage:
    """Tackling with common pages functions in header and footer"""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def start(self):
        self.page.goto(self.base_url)
        return self

    def search(self, keyword: str):
        self.page.locator('input[name="search"]').fill(keyword)
        self.page.locator('input[name="search"]').press("Enter")
        return SearchPage(self.page, self.base_url)

    # TODO мб сразу open?
    def get_basket_widget(self):
        return self.page.locator("#header-cart")

    def change_currency(self, currency: str):
        self.page.locator("form#form-currency button").click()
        self.page.locator(
            f"form#form-currency button:has-text('{currency}')"
        ).click()

    def go2cart(self):
        widget = self.get_basket_widget()
        widget.locator("button").click()
        widget.locator("a[href*='route=checkout/cart']").wait_for(
            state="visible"
        )
        widget.locator("a[href*='route=checkout/cart']").click()
        return CartPage(self.page, self.base_url)
