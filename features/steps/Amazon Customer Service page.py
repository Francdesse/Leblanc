from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_LINK = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')

@given('Open Amazon T&C page')
def nav_to_cust_serv_Page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/'
                       'ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when ('Store original windows')
def storing_original_window(context):
    context.original_window= context.driver.current_window_handle

@when('Click on Amazon Privacy Notice link')
def clicking_on_privacy_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when('Switch to the newly opened window') #switching to the new page
def Switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows= context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])

@then('Verify Amazon Privacy Notice page is opened')
def amz_pri_page_opens(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer'))


@then('close Privacy notice page') #this will close the pop up open tab
def closing_privacy_notice_page(context):
    context.driver.close()
@then('switch back to original') #switch back to original page
def closing_new_window_and_switching_to_original(context):
    context.driver.switch_to.window(context.original_window)
