from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    CLICKING_ON_ADD_TO_CART = (By.ID, 'add-to-cart-button')
    DECLINE_COVERAGE = (By.CSS_SELECTOR, '#attachSiNoCoverage input.a-button-input')
    def user_add_item_to_cart(self):
        self.click(*self.CLICKING_ON_ADD_TO_CART)

    def user_decline_protection(self):
        self.click(*self.DECLINE_COVERAGE)