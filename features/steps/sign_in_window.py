from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CONDITIONS_OF_USE = (By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088']")


@given("store original window")
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when("user clicks on conditions of use")
def clicking_on_conditions_of_use(context):
    context.driver.find_element(*CONDITIONS_OF_USE).click()

    #sleep(2)


@when("switch to new window")
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1]) #switching to the second window