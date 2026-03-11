from behave import given, when, then

@then('verify cart is {empty}')
def verify_cart_is_empty(context, empty):
    context.app.cart_page.verify_cart_is_empty(empty)