from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


PAGE_TITLE = (By.XPATH, "//h1[text()='Conditions of Use']")


@then('verify the condition page is open')
def verify_condition_page(context):
    context.driver.wait.until(EC.url_contains('help/customer/display.html/ref=ap'))


@then('close conditions page')
def close_web_menu(context):
    context.driver.close()


@then('return to original window')
def returning_to_original_window(context):
    context.driver.switch_to.window(context.original_window)