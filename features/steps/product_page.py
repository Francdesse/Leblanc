from behave import given, when, then


@then('verify that iphone is in the title')
def verify_that_it_opens_selected_product_page(context):
    context.app.product_page.verify_that_iphone_is_in_the_title()

