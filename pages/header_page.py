from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
class Header(Page):
    SEARCH_FOR_ITEM = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    CLICK_ON_CART = (By.ID, 'nav-cart-count-container')
    PROCESS_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, '[name="proceedToRetailCheckout"]')
    CLICK_ON_ORDERS = (By.XPATH, "//a[contains(@href, 'nav_orders_first')]")
    BEST_SELLER_LINK = (By.CSS_SELECTOR, '[data-csa-c-content-id="nav_cs_bestsellers"]')
    def search_for_product(self):
        self.input_text('apple mouse', *self.SEARCH_FOR_ITEM)

    def user_clicks_on_search_button(self):
        self.click(*self.SEARCH_BUTTON)

    def user_clicks_on_cart(self):
        #self.wait_for_element_click(self.PROCESS_TO_CHECKOUT_BTN)
        self.click(*self.CLICK_ON_CART)

    def click_on_orders(self):
        self.click(*self.CLICK_ON_ORDERS)

    def user_clicks_and_open_best_seller_page(self):
        #self.wait_for_element_click(self.BEST_SELLER_LINK)
        self.click(*self.BEST_SELLER_LINK)