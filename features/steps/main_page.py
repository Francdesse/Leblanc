from behave import given, when, then


@given('user go to amazon')
def user_nav_to_site(context):
    context.app.main_page.user_nav_to_site()


@when('search for {searchText}')#{searchText- is the title name for the search item from the feature file aka "iphone"}
def step_impl(context,searchText):
    context.app.main_page.user_search_item(searchText)
