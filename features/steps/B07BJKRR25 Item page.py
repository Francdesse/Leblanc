from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('user navigate to product page {product_id}')
def nav_amazon_page(context, product_id):
    context.app.search_results.nav_amazon_page(product_id)


@then ('verify all items are functional')
def items_are_functional(context):
    context.app.product_page.items_are_functional()




