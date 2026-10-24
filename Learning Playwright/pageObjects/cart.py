class CartPage:

    def __init__(self, page):
        self.page = page

    def checkingOutitem(self):
        self.page.get_by_role("button", name="Checkout").click()
        self.page.sleep(2)
        self.page.locator('.form-group .input.txt.text-validated').fill("United States")
        # page.get_by_role("button", name="United States").click()
        # sleep(2)
        self.page.locator('.btnn.action__submit.ng-star-inserted').click()
        self.page.sleep(2)

    def orderConfirmationMsg(self):
        order_confirmation = self.page.get_by_text("Thank you, your order has been placed successfully.")
        assert order_confirmation
        self.page.sleep(5)

        # verifying order# by comparing order number and api order number
        self.page.get_by_role("button", name="ORDERS").click()
        self.page.sleep(2)