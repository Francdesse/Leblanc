from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGNIN_PAGE = (By.XPATH, "//h1[@class='a-spacing-small']")

@then('Verify user is taken to the sign in page')
def load_sign_in_page(context):
    expected_result = "Sign in"
    actual_result1 = context.driver.find_element(*SIGNIN_PAGE).text
    assert expected_result == actual_result1













