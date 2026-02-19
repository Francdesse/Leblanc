from behave import given, when, then

@given('user_go_to_amazon')
def step_impl(context):
    print("user_go_to_amazon")

@when('search for "iphone"')
def step_impl(context):
    print("search for iphone")

@then('iphone is showned in the search')
def step_impl(context):
    print('iphone is showned in the search')