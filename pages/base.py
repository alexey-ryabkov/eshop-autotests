import allure
from playwright.sync_api import Page


class BasePage:
    """Tackling with common pages functions in header and footer"""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def _start(self):
        self.page.goto(self.base_url)
        return self

    def search(self, keyword: str):
        from .search import SearchPage

        search_input = self.get_search_input()
        submit_button = search_input.locator("xpath=following-sibling::button")
        with allure.step(f"Search for {keyword}"):
            search_input.fill(keyword)
            submit_button.click()

        return SearchPage(self.page, self.base_url)

    def change_currency(self, currency: str):
        currency_selector = self.get_currency_selector()
        currency_ctrl = currency_selector.locator(f"a[href*='{currency}']")
        with allure.step("Click on the currency selector"):
            currency_selector.click()
        currency_ctrl.wait_for(state="visible")
        with allure.step(f"Select {currency} currency"):
            currency_ctrl.click()

    def go2cart(self):
        from .cart import CartPage

        with allure.step("Navigate to cart page"):
            self.get_top_nav_links().locator(
                "a:has-text('Shopping Cart')"
            ).click()
        return CartPage(self.page, self.base_url)

    def wait_4notification(self, allure_step="Wait for notification"):
        notification = self.get_notification()
        with allure.step(allure_step):
            notification.wait_for(state="visible")
        return notification

    def get_cart_button(self):
        return self.get_cart_widget().locator("button").first

    def get_cart_widget(self):
        return self.page.locator("#header-cart")

    def get_currency_selector(self):
        return self.page.locator("form#form-currency")

    def get_top_nav_links(self):
        return self.page.locator("#top .nav:nth-child(2)")

    def get_notification(self):
        return self.page.locator("#alert")

    def get_search_input(self):
        return self.page.locator("#search input[name='search']")
