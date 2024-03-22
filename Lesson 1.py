from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service=Service(driver_path)
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid."
           "return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.iden"
           "tity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc"
           "_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid"
           ".net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

driver.find_element(By.ID,"ap_email").send_keys("francyoudesse@icloud.com")
sleep(5)
driver.find_element(By.ID, "continue").click()
sleep(5)
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']" ).click()
print('complete')