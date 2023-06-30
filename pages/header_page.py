from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
class Header(Page):
    SEARCH_FOR_ITEM = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    CLICK_ON_CART = (By.ID, 'nav-cart-count-container')
    PROCESS_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, '[name="proceedToRetailCheckout"]')
    CLICK_ON_ORDERS = (By.XPATH, "//a[contains(@href, 'nav_orders_first')]")
    BEST_SELLER_LINK = (By.CSS_SELECTOR, '[data-csa-c-content-id="nav_cs_bestsellers"]')
    NUMB_ABOVE_CART = (By.ID, 'nav-cart-count')
    DEPARTMENT = (By.ID, 'searchDropdownBox')
    SEARCH_BOX =(By.ID, 'twotabsearchtextbox')

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

    def User_sees_1_above_cart(self):
        self.verify_element_text('1', *self.NUMB_ABOVE_CART)

    def user_clicks_on_dropdown_and_choose_dep(self):
        dept_select = self.find_element(*self.DEPARTMENT)
        select = Select(dept_select)
        select.select_by_value('search-alias=videogames')


    def user_search(self, search_id):
        self.input_text(search_id, *self.SEARCH_BOX)

    def user_search_for_cofee(self, search_ID):
        self.input_text(search_ID, *self.SEARCH_BOX)