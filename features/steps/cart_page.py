from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, '.a-row .sc-your-amazon-cart-is-empty')
FIND_MOUSE_IN_CART = (By.CSS_SELECTOR, '.a-truncate-cut')

@then('cart is empty message')
def verify_user_sees_empty_cart(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result= context.driver.find_element(*EMPTY_CART_MESSAGE).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'



@then('verify apple mouse is in cart')
def User_sees_apple_mouse_in_cart(context):
    sleep(5)
    actual_result = context.driver.find_element(*FIND_MOUSE_IN_CART).text
    assert context.product_name[:30] in actual_result, f'Error! {actual_result} is not the same as {context.product_name}'


