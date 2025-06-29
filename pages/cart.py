import re
import allure

from .base import BasePage


class CartPage(BasePage):
    def open(self):
        self._start()
        return self.go2cart()

    def change_quantity(self, product: str, quantity: int = 1):
        product_item = self.get_cart_item(product)
        with allure.step(f"Change quantity for {product}"):
            qty_input = product_item.locator("input[name*='quantity']")
            qty_input.fill(str(quantity))
        with allure.step(f"Refresh {product} cart item"):
            product_item.locator("button[title='Update']").click()
            self._wait_4update()

    def clear(self):
        product_items = self.get_cart_table().locator("tbody tr")
        count = product_items.count()
        for i in range(count):
            with allure.step(f"Delete product #{i} from the cart"):
                product_items.nth(i).locator(
                    "button[aria-label='Remove']"
                ).click()
                self._wait_4update()

    def get_cart_item_price(self, product: str):
        product_item = self.get_cart_item(product)
        raw_price = product_item.locator("text-end").last.text_content
        return self._parse_price(raw_price)

    def get_cart_item(self, product: str):
        return self.get_cart_table().locator(f"tbody tr:has-text('{product}')")

    def get_cart_table(self):
        return self.page.locator("#shopping-cart .table")

    @staticmethod
    def _parse_price(text: str) -> float:
        price = re.sub(r"[^\d.,]", "", text)

        if "," in price and "." in price:
            price = price.replace(",", "")
        elif "," in price:
            price = price.replace(",", ".")

        return float(price)

    def _wait_4update(self):
        self.page.wait_for_load_state("networkidle")
