from .cartPage import CartPage

class DashboardPage:

    def __init__(self, page):
        self.page = page

    def addingItemtoCart(self):
        item_tile = self.page.get_by_text("ADIDAS ORIGINAL").text_content()
        self.page.locator('#products > div.container > div.row > div:nth-child(1) > div > div > button.btn.w-10.rounded').click()
        self.page.sleep(5)
        self.page.locator("button.btn-custom[routerlink='/dashboard/cart']").click()
        self.page.sleep(2)
        cart_item = self.page.locator(".cartSection h3").text_content()
        assert item_tile == cart_item
        self.page.sleep(2)

        cartPage = CartPage(self.page)
        return cartPage