from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_BOX = (By.CSS_SELECTOR, '.search-input')
SEARCH_BTN = (By.CSS_SELECTOR, '[alt="search"].search-btn')
TRACK_ORDER = (By.XPATH, "//div[text()='track an order']")
SITE_HEADER = (By.XPATH, "//h2[@class ='custom-h2']")


@given('user navigates to {search_link}')
def user_navigates_to_link(context, search_link):
    context.driver.get(search_link)


@then('verify all elements are present')
def verify_all_elements_present(context):
    assert context.driver.find_element(*SEARCH_BOX).is_displayed(), f'{SEARCH_BOX} is not displayed'
    assert context.driver.find_element(*SEARCH_BTN).is_displayed(), f'{SEARCH_BTN} is not displayed'
    assert context.driver.find_element(*TRACK_ORDER).is_displayed(), f'{TRACK_ORDER} is not displayed'
    assert context.driver.find_element(*SITE_HEADER).is_displayed(), f'{SITE_HEADER} is not displayed'
