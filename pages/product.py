import allure

from .base import BasePage


class ProductPage(BasePage):
    def open(self, product: str):
        self._start()
        return self.search(product).go_2first_result()

    def open_gallery(self):
        with allure.step(
            "Open product gallery by clicking on one of the product`s photo"
        ):
            self.page.locator(".magnific-popup a").first.click()

    def get_gallery(self):
        return self.page.locator(".mfp-gallery")
