from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com')


@when('Clicks on orders')
def click_on_orders(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'nav_orders_first')]").click()


@then('Verify user is taken to the sign in page')
def load_sign_in_page(context):
    expected_result = "Sign in"
    actual_result1 = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result1


@when('click on cart')
def user_clicks_on_cart(context):
    from time import sleep
    sleep(10)
    # context.driver.find_element(By.ID, 'nav-cart').click()
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()



@then('cart is empty message')
def verify_user_sees_empty_cart(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result= context.driver.find_element(By.CSS_SELECTOR, '.a-row .sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'

@when('search for an apple mouse')
def search_for_item(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('apple mouse')


@when('click search button')
def user_clicks_on_search_button(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@then('verify item is in double quotes')
def items_are_in_double_quotation(context):
    expected_result = '"apple mouse"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'

@when('click on the first result')
def user_click_on_search_button(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

    context.driver.find_element(By.XPATH, "//div[@data-asin='B09BRD98T4']"
                                          "//div[@class='sg-row']//a[contains"
                                          "(@href,'/Apple-Magic-Mouse-Wireless-Re') "
                                          "and @class='a-link-normal s-underline-text"
                                          " s-underline-link-text s-link-style a-text-normal']").click()


@when('click on add to cart')
def user_add_item_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()
@when('decline coverage protection')
def user_decline_protection(context):
    context.driver.find_element(By.CSS_SELECTOR, '#attachSiNoCoverage input.a-button-input').click()

    from time import sleep
    sleep(6)

@then('verify added to cart message')
def user_sees_added_to_cart_message(context):
    expected_result = 'Added to Cart'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-fixed-left-grid-inner .a-text-bold').text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'

    from time import sleep
    sleep(10)



@then('verify apple mouse is in cart')
def User_sees_apple_mouse_in_cart(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-truncate-cut').is_displayed(), 'Apple mouse not found'


@then('verify that cart has 1 item')
def User_sees_1_above_cart(context):
    expected_result = '1'
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'
