from behave import given, when, then


@then('verify that product name is the same as product title')
def verify_that_it_opens_selected_product_page(context):
    context.app.product_page.verify_that_product_name_is_the_same_as_product_title()

