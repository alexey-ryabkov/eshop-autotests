import allure

from .base import BasePage
from .product import ProductPage


class SearchPage(BasePage):
    def open(self):
        self._start()
        return self.search("")

    # Here is a simplification, sufficient for this project
    # that we are only searching for products
    def go_2first_result(self):
        keyword = self.get_search_input().input_value
        results_list = self.get_results_list()
        with allure.step(f"Open the first found result for {keyword}"):
            results_list.locator(".product-thumb h4 a").first.click()
        return ProductPage(self.page, self.base_url)

    def get_results_list(self):
        return self.page.locator("#product-list")
