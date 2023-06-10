from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


KEYWORD_SEARCH_IN_DOUBLE_QUOTE = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
CLICKING_ON_SEARCH_BTN = (By.ID, 'nav-search-submit-button')
APPLE_MOUSE = (By.XPATH, "//div[@data-asin='B09BRD98T4']"
                                          "//div[@class='sg-row']//a[contains"
                                          "(@href,'/Apple-Magic-Mouse-Wireless-Re') "
                                          "and @class='a-link-normal s-underline-text"
                                          " s-underline-link-text s-link-style a-text-normal']")
#APPLE_MOUSE_TITLE = (By.XPATH, "//span[text()='Apple Magics Mouse: Wireless, Bluetooth, Rechargeable. Works with Mac or iPad; Multi-Touch Surface - White']")
APPLE_MOUSE_TITLE = (By.ID, "productTitle")

@then('verify item is in double quotes')
def items_are_in_double_quotation(context):
    # expected_result = '"apple mouse"'
    # actual_result = context.driver.find_element(*KEYWORD_SEARCH_IN_DOUBLE_QUOTE).text
    # assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'
    context.app.search_results.items_are_in_double_quotation()

@when('click on the first result')
def user_click_on_search_button(context):
    # context.driver.find_element(*CLICKING_ON_SEARCH_BTN).click()
    # context.driver.find_element(*APPLE_MOUSE).click()
    context.app.search_results.user_click_on_search_button()

@when('store item title')
def store_prod_name(context):
    context.product_name = context.driver.find_element(*APPLE_MOUSE_TITLE).text
    print(f'current product: {context.product_name}')
