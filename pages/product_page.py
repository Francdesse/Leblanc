from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage(Page):
    CLICKING_ON_ADD_TO_CART = (By.ID, 'add-to-cart-button')
    DECLINE_COVERAGE = (By.CSS_SELECTOR, '#attachSiNoCoverage input.a-button-input')
    APPLE_MOUSE_TITLE = (By.ID, "productTitle")
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#attach-added-to-cart-alert-and-image-area .a-alert-heading')
    COLOR_VARIATIONS = (By.CSS_SELECTOR, '#variation_color_name li')
    CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
    CLOSE_PROD_BOX = (By.ID, 'attach-close_sideSheet-link')
    NEW_ARRIVAL = (By.CSS_SELECTOR, '#nav-subnav [href*="/New-Arrivals"]')
    BABY_SUB_MENU = (By.CSS_SELECTOR, '[href*="/s?i=fashion-baby"]')
    ONE_TIME_PAYMENT = (By.ID, 'newAccordionCaption_feature_div')
    def user_add_item_to_cart(self):
        self.click(*self.CLICKING_ON_ADD_TO_CART)

    def user_decline_protection(self):
        self.click(*self.DECLINE_COVERAGE)

    def user_X_out_ofwindow(self):
        self.click(*self.CLOSE_PROD_BOX)

    def store_prod_name(self):
        self.driver.product_name = self.driver.find_element(*self.APPLE_MOUSE_TITLE).text
        print(f'current product: {self.driver.product_name}')

    def user_sees_added_to_cart_message(self):
        sleep(2)
        self.verify_element_text('Added to Cart', *self.ADDED_TO_CART_MESSAGE)

    def items_are_functional(self):
        expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed']
        actual_colors = []

        # colors = context.driver.find_elements(*COLOR_VARIATIONS)

        for i in range(5):
            color = self.driver.find_elements(*self.COLOR_VARIATIONS)[i]
            color.click()
            current_color = self.driver.find_element(*self.CURRENT_COLOR).text
            actual_colors += [current_color]

            # image = context.driver.find_elements(*YOUR_LOCATOR)[i]
            # image.is_displayed()

        assert expected_colors == actual_colors, \
            f'Expected colors {expected_colors} did not match actual {actual_colors}'

    def user_hover_over_menu(self):
        new_arrival_option = self.find_element(*self.NEW_ARRIVAL)

        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(*self.NEW_ARRIVAL))
        actions.perform()

    def baby_sec_present(self):
        self.wait_for_element_appear(*self.BABY_SUB_MENU)

    def user_clicks_one_time_payment(self):
        self.click(*self.ONE_TIME_PAYMENT)
