from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service=Service(driver_path)
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2"
           "Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.as"
           "soc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fide"
           "ntifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sleep(8)
driver.find_element(By.ID,"ap_email").send_keys("francyoudesse@icloud.com")
sleep(5)
# finding elemment with ID
driver.find_element(By.ID, "continue").click()
sleep(5)
# finding elemment with short xpath
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']" ).click()
driver.back()
sleep(8)
# finding elemment with contains
driver.find_element(By.XPATH, "//a[contains(@href, 'ref=ap_signin_notification_condition_of_use?')]").click()
expected = "Conditions of Use"
actual = driver.find_element(By.XPATH, "//h1[text()='Conditions of Use']").text
print(actual)
assert expected == actual, f'{expected} does not equal to {actual}'

driver.back()
sleep(8)
driver.find_element(By.XPATH, "//a[contains (@href,'html/ref=ap_signin_notification_privacy_notice?')]").click()
expected="Amazon.com Privacy Notice"
actual=driver.find_element(By.XPATH, "//h1[text()='Amazon.com Privacy Notice']").text
assert expected == actual, f'{expected} does not equal to{actual}'

print('complete')

driver.quit()