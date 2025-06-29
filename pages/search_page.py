from pages.base_page import BasePage
from pages.product_page import ProductPage


class SearchPage(BasePage):
    def open(self):
        return self.search("")

    def go2first_result(self):
        self.page.locator(".product-thumb h4 a").first.click()
        return ProductPage(self.page, self.base_url)
