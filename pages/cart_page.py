from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART_MESSAGE = (By.XPATH, "//div//h3[contains(text(), 'Your Amazon Cart')]")

    def verify_cart_is_empty(self, text):
        msg = self.find_element(*self.EMPTY_CART_MESSAGE).text
        print(f'Cart message: {msg}')
        assert text in msg, f'{text} is not in {msg}'
