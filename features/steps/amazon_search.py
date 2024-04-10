from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
CART = (By.ID, 'nav-cart-count-container')
SEARCH_FIELD = (By.ID, "twotabsearchtextbox")
POP_UP_LOGIN_BTX = (By.CSS_SELECTOR, '#nav-signin-tooltip [href*="signin?openid.pape.max_auth_age=0&openid.return"]')
SIGN_IN_TEXT = (By.CSS_SELECTOR,'#continue.a-button.a-button-primary')


@given('user launch amazon site')
def user_launch_amazon(context):
    context.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_"
                       "to=https%3A%2F%2Fwww.amazon.com%2Ffmc%2Flearn-more%3Fref_%3Dnav_signin&openid.ident"
                       "ity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usfle"
                       "x&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fid"
                       "entifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")


@when('user search for {search_word}')
def user_search_coffee(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys("coffee")


@when('user clicks on search button')
def user_search_button(context):
    context.driver.find_element(*SEARCH_BUTTON).click()


@when('user clicks on cart')
def user_click_cart(context):
    context.driver.find_element(*CART).click()
    sleep(5)


@when('verify that the login popup box comes up')
def user_sees_login_popup(context):
    assert context.driver.wait.until(EC.element_to_be_clickable(POP_UP_LOGIN_BTX)), f'pop box did not show up'


@when('user click on signin popup')
def user_click_signin_popup(context):
    context.driver.wait.until(EC.element_to_be_clickable((POP_UP_LOGIN_BTX))).click()


@then('verify that user sees {expected_result}')
def verify_coffee(context, expected_result):
    actual = context.driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text

    assert expected_result == actual, f'expected search "{expected_result}" but got {actual}'


@then('verify that user is in the sign in page')
def verify_user_sees_login_page(context):
    context.driver.wait.until(EC.presence_of_element_located(SIGN_IN_TEXT))
    print('complete')