from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('verify {empty_cart_message} message')
def verify_cart_message(context, empty_cart_message):
    actual_message = context.driver.find_element(By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty, h1').text
    assert empty_cart_message == actual_message, f'expected {empty_cart_message} but got {actual_message}'