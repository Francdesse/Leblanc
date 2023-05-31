from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


CLICKING_ON_ADD_TO_CART = (By.ID, 'add-to-cart-button')
DECLINE_COVERAGE = (By.CSS_SELECTOR, '#attachSiNoCoverage input.a-button-input')
#ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, '.a-fixed-left-grid-inner .a-text-bold')
ADDED_TO_CART_MESSAGE = (By.XPATH, "//div[@id='NATC_SMART_WAGON_CONF_MSG_SUCCESS']/span")
SIGN_INTO_ACC_BTN = (By.CSS_SELECTOR, '#a-autoid-0-announce')

@when('click on add to cart')
def user_add_item_to_cart(context):
    context.driver.find_element(*CLICKING_ON_ADD_TO_CART).click()



@when('decline coverage protection')
def user_decline_protection(context):
    context.driver.wait.until(EC.element_to_be_clickable(context.driver.find_element(*DECLINE_COVERAGE))).click()



@then('verify added to cart message')
def user_sees_added_to_cart_message(context):
    #context.driver.wait.until(EC.element_to_be_clickable(SIGN_INTO_ACC_BTN))
    expected_result = 'Added to Cart'
    actual_result = context.driver.find_element(*ADDED_TO_CART_MESSAGE).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'

    #sleep(10)
