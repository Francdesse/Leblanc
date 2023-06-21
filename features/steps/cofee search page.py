from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('user navigate to product page')
def open_amazon_page(context):
    context.app.search_results.open_amazon_page()

@then ('verify all product names are present & verify all product image are present')
def img_and_work_present(context):
    context.app.search_results.img_and_work_present()