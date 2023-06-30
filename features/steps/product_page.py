from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC



@when('click on add to cart')
def user_add_item_to_cart(context):
    context.app.product_page.user_add_item_to_cart()



@when('decline coverage protection')
def user_decline_protection(context):
    context.app.product_page.user_decline_protection()

@when('close window')
def user_X_out_ofwindow(context):
    context.app.product_page.user_X_out_ofwindow()

@when('user hover over new arrival')
def user_hover_over_menu(context):
    context.app.product_page.user_hover_over_menu()

@when('click on One time payment')
def user_clicks_one_time_payment(context):
    context.app.product_page.user_clicks_one_time_payment()

@then('verify added to cart message')
def user_sees_added_to_cart_message(context):
    context.app.product_page.user_sees_added_to_cart_message()



@then('verify that user baby item is present')
def baby_sec_present(context):
    context.app.product_page.baby_sec_present()




