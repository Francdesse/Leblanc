from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


CLICK_ON_ORDERS = (By.XPATH, "//a[contains(@href, 'nav_orders_first')]")
CLICK_ON_CART = (By.ID, 'nav-cart-count-container')
SEARCH_FOR_ITEM = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
NUMB_ABOVE_CART = (By.ID, 'nav-cart-count')
PROCESS_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, '[name="proceedToRetailCheckout"]')

@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com')

@when('Clicks on orders')
def click_on_orders(context):
    context.driver.find_element(*CLICK_ON_ORDERS).click()



@when('click on cart')
def user_clicks_on_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(PROCESS_TO_CHECKOUT_BTN))
    context.driver.find_element(*CLICK_ON_CART).click()


@when('search for an apple mouse')
def search_for_item(context):
    context.driver.find_element(*SEARCH_FOR_ITEM).send_keys('apple mouse')


@when('click search button')
def user_clicks_on_search_button(context):
    context.driver.find_element(*SEARCH_BUTTON).click()


@then('verify that cart has 1 item')
def User_sees_1_above_cart(context):
    expected_result = '1'
    actual_result = context.driver.find_element(*NUMB_ABOVE_CART).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'