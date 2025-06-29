from pages.base_page import BasePage
from pages.home_page import HomePage


class ProductPage(BasePage):
    def open(self, product: str):
        return HomePage(self.page, self.base_url).open().go2product(product)

    def open_gallery(self):
        self.page.locator(".image a").first.click()

    def get_gallery(self):
        return self.page.locator(".mfp-figure")
