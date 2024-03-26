from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('user launch amazon site')
def user_launch_amazon(context):
    context.driver.get("https://amazon.com")


@when('user search for {search_word}')
def user_search_coffee(context, search_word):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("coffee")


@when('user clicks on search button')
def user_search_button(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


sleep(5)


@then('verify that user sees {expected_result}')
def verify_coffee(context, expected_result):
    actual = context.driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text

    assert expected_result == actual, f'expected search "{expected}" but got {actual}'


print('complete')