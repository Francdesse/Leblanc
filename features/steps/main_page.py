from behave import given, when, then


@given('user go to amazon')
def user_nav_to_site(context):
    context.app.main_page.user_nav_to_site()


@when('search for {searchText}')#{searchText- is the title name for the search item from the feature file aka "iphone"}
def step_impl(context, searchText):
    context.app.main_page.user_search_item(searchText)

@when('clicks on search button')
def user_clicks_on_search_btn(context):
    context.app.main_page.user_click_search_btn()

@when('selecting third item from search result')
def selecting_third_item_from_search_result(context):
    context.app.main_page.selecting_third_item_from_search_result()

@then('{searchText} is showned in the search result')
def verify_search_item(context, searchText):
    context.app.main_page.search_item_is_shown(searchText)

@then('verify each links are clickable')
def verify_each_links_are_clickable(context):
    context.app.main_page.verify_each_links_are_clickable()