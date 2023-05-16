from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HEADER_MESSAGE= (By.CSS_SELECTOR, 'h1.fs-heading')
LIST_OF_LINKS = (By.CSS_SELECTOR, '.issue-card-container .issue-card-wrapper')
SEARCH_BAR_TITLE = (By.XPATH, '//h2[text()= "Search our help library"]')
SEARCH_BAR = (By.ID, 'hubHelpSearchInput')
HELP_HEADER = (By.XPATH, "//h2[text()='All help topics']")
HELP_TOPIC_LINKS = (By.CSS_SELECTOR, 'li.help-topics')

@given('navigate to the customer service page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/hz/contact-us/foresight/hubgateway')


@then('verify user sees Welcome to Amazon customer service')
def user_sees_welcome_message(context):
    expected_header = 'Welcome to Amazon Customer Service'
    actual_header = context.driver.find_element(*HEADER_MESSAGE).text
    assert expected_header == actual_header, f'Error! {expected_header} is not the same as {actual_header}'



@then('verify that there are 10 links on the page')
def links_on_top_menu(context):
    count_links = len(context.driver.find_elements(*LIST_OF_LINKS))
    assert count_links > 7, f'Error! {count_links} is not greater than 7'
    print(count_links, (context.driver.find_elements(*LIST_OF_LINKS)))

@then('verify the search bar title is present')
def search_bar_title(context):
    expected_result = 'Search our help library'
    actual_result = context.driver.find_element(*SEARCH_BAR_TITLE).text
    assert expected_result == actual_result, f'Error! {expected_result} does not equal to {actual_result}'


@then('verify the search bar is present')
def search_bar_present(context):
    context.driver.find_element(*SEARCH_BAR).is_displayed();'Error! search box not found'


@then('verify that user sees All help topics')
def sees_help_topics_header(context):
    expected_result = 'All help topics'
    actual_result = context.driver.find_element(*HELP_HEADER).text
    assert expected_result == actual_result, f'Error! {expected_result} does not equal to {actual_result}'


@then('verify that user sees 11 links under help topics')
def user_sees_11_links(context):
    count_links = len(context.driver.find_elements(*HELP_TOPIC_LINKS))
    assert count_links >= 7
    print(count_links, (context.driver.find_elements(*HELP_TOPIC_LINKS)))