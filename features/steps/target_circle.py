from selenium.webdriver.common.by import By
from behave import given, when, then

ELEMENTS_LIST = (By.CSS_SELECTOR, 'li.styles__BenefitCard-sc-9mx6dj-2')


@given('user navigate to {search_link}')
def user_navigates_to_link(context, search_link):
    context.driver.get(search_link)


@then('verify there are {num_element} elements present')
def verify_num_element(context, num_element):
    num_element = int(num_element)
    actual_num_elements = (context.driver.find_elements(*ELEMENTS_LIST))
    assert len(actual_num_elements) == num_element, f'Expected {num_element} does not equal to {actual_num_elements}'