from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('verify item is in double quotes')
def items_are_in_double_quotation(context):
    context.app.search_results.items_are_in_double_quotation()

@when('click on the first result')
def user_click_on_search_button(context):
    context.app.search_results.user_click_on_search_button()

@when('store item title')
def store_prod_name(context):
    context.app.product_page.store_prod_name()

@when('click on an item')
def user_clicks_on_item(context):
    context.app.search_results.user_clicks_on_item()
@then('verify user sees video games')
def user_sees_video_games(context):
    context.app.search_results.user_sees_video_games()


