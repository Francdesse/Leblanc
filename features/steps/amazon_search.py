from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
CART = (By.ID, 'nav-cart-count-container')
SEARCH_FIELD = (By.ID, "twotabsearchtextbox")


@given('user launch amazon site')
def user_launch_amazon(context):
    context.driver.get("https://amazon.com")


@when('user search for {search_word}')
def user_search_coffee(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys("coffee")


@when('user clicks on search button')
def user_search_button(context):
    context.driver.find_element(*SEARCH_BUTTON).click()


@when('user clicks on cart')
def user_click_cart(context):
    context.driver.find_element(*CART).click()
    sleep(5)


@then('verify that user sees {expected_result}')
def verify_coffee(context, expected_result):
    actual = context.driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text

    assert expected_result == actual, f'expected search "{expected_result}" but got {actual}'

    print('complete')