from pages.base_page import BasePage
from pages.product_page import ProductPage


class HomePage(BasePage):
    def open(self):
        return self.start()

    def get_slider(self):
        return self.page.locator("#carousel")

    def get_products(self):
        return self.page.locator("#products")

    def go2product(self, product: str):
        self.get_products().locator(f"text={product}").first.click()
        return ProductPage(self.page, self.base_url)
