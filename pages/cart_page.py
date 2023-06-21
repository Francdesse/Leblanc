from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class CartPage(Page):
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, '.a-row .sc-your-amazon-cart-is-empty')
    FIND_MOUSE_IN_CART = (By.CSS_SELECTOR, '.a-truncate-cut')
    APPLE_MOUSE_TITLE = (By.ID, "productTitle")
    def verify_user_sees_empty_cart(self):
        self.verify_element_text('Your Amazon Cart is empty', *self.EMPTY_CART_MESSAGE)

    def User_sees_apple_mouse_in_cart(self):
        # sleep(5)
        # product_name = self.driver.find_element(*self.APPLE_MOUSE_TITLE).text
        actual_result = self.driver.find_element(*self.FIND_MOUSE_IN_CART).text
        assert self.driver.product_name[:30] in actual_result, f'Error! {actual_result} is not the same as {self.product_name}'