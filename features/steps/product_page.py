from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


CLICKING_ON_ADD_TO_CART = (By.ID, 'add-to-cart-button')
DECLINE_COVERAGE = (By.CSS_SELECTOR, '#attachSiNoCoverage input.a-button-input')
ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#attach-added-to-cart-alert-and-image-area .sw-atc-text ')
PROCEED_TO_CHECKOUT = (By.ID, 'sc-buy-box-ptc-button')

@when('click on add to cart')
def user_add_item_to_cart(context):
    # context.driver.find_element(*CLICKING_ON_ADD_TO_CART).click()
    context.app.product_page.user_add_item_to_cart()



@when('decline coverage protection')
def user_decline_protection(context):
    # context.driver.wait.until(EC.element_to_be_clickable(context.driver.find_element(*DECLINE_COVERAGE))).click()
    context.app.product_page.user_decline_protection()

@when('close window')
def user_X_out_ofwindow(context):
    context.app.product_page.user_X_out_ofwindow()

@when('user hover over new arrival')
def user_hover_over_menu(context):
    context.app.product_page.user_hover_over_menu()

@then('verify added to cart message')
def user_sees_added_to_cart_message(context):
    #context.driver.wait.until(EC.element_to_be_clickable(PROCEED_TO_CHECKOUT))
    context.app.product_page.user_sees_added_to_cart_message()

@then('verify that user baby item is present')
def baby_sec_present(context):
    context.app.product_page.baby_sec_present()


