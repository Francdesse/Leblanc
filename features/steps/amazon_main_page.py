from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@given('Open Amazon page')
def open_amazon_page(context):
    context.app.main_page.open_amazon_page()

@when('Clicks on orders')
def click_on_orders(context):
    context.app.header_page.click_on_orders()



@when('click on cart')
def user_clicks_on_cart(context):
    sleep(3)
    context.app.header_page.user_clicks_on_cart()



@when('search for an apple mouse')
def search_for_item(context):
    context.app.header_page.search_for_product()


@when('click search button')
def user_clicks_on_search_button(context):
    context.app.header_page.user_clicks_on_search_button()


@then('verify that cart has 1 item')
def User_sees_1_above_cart(context):
    context.app.header_page.User_sees_1_above_cart()


@when('Click on dropdown and choose a dept')
def user_clicks_on_dropdown_and_choose_dep(context):
    context.app.header_page.user_clicks_on_dropdown_and_choose_dep()

@when('user search for {search_id}')
def user_search(context, search_id):
     context.app.header_page.user_search(search_id)

@when('search {search_ID}')
def user_search_for_cofee(context, search_ID):
    context.app.header_page.user_search_for_cofee(search_ID)

