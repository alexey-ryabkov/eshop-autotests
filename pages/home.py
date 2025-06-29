import allure

from .base import BasePage


class HomePage(BasePage):
    def open(self):
        with allure.step("Go to the eshop homepage"):
            return self._start()

    def add_product_2cart(self, product: str):
        with allure.step(f"Click on cart button for {product} product"):
            product_card = self.get_product_card(product)
            product_card.locator("button").first.click()
        self.wait_4notification("Wait for cart alert to appear")

    def get_product_card(self, title: str):
        return self.page.locator(f"#content .product-thumb:has-text('{title}')")

    def get_carousel(self):
        return self.page.locator("#carousel-banner-0")
