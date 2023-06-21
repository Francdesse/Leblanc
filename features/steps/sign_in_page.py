from selenium.webdriver.common.by import By
from behave import given, when, then



@then('Verify user is taken to the sign in page')
def load_sign_in_page(context):
    context.app.sign_in_page.load_sign_in_page()













