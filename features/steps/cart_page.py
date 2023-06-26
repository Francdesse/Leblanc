from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('cart is empty message')
def verify_user_sees_empty_cart(context):
    context.app.cart_page.verify_user_sees_empty_cart()


@then('verify apple mouse is in cart')
def User_sees_apple_mouse_in_cart(context):
    context.app.cart_page.User_sees_apple_mouse_in_cart()

