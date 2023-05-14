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

@then('verify item is in double quotes')
def items_are_in_double_quotation(context):
    expected_result = '"apple mouse"'
    actual_result = context.driver.find_element(*KEYWORD_SEARCH_IN_DOUBLE_QUOTE).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'


@when('click on the first result')
def user_click_on_search_button(context):
    context.driver.find_element(*CLICKING_ON_SEARCH_BTN).click()

    context.driver.find_element(*APPLE_MOUSE).click()


