from .base_page import BasePage


class CartPage(BasePage):
    def open(self):
        return self.go2cart()

    def change_quantity(self, product: str, quantity: int = 1):
        row = self.page.locator(
            f"//div[@id='content']//tr[.//a[contains(text(), '{product}')]]"
        )
        qty_input = row.locator("input[name*='quantity']")
        qty_input.fill(str(quantity))
        row.locator("button[data-original-title='Update']").click()
        self.page.wait_for_load_state("networkidle")

    def clear(self):
        rows = self.page.locator("#content .table-responsive tbody tr")
        count = rows.count()
        for i in range(count):
            rows.nth(i).locator("button[data-original-title='Remove']").click()
            self.page.wait_for_load_state("networkidle")
