from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


# open the url and to go QA automation page
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.'
           'max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth'
           '%2F2.0%2Fidentifier_select&pageId=usflex&mobileBrowserWeblabTreatment'
           '=C&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fregistration%2Fs%3F'
           'k%3Dregistration%26ref_%3Dnav_ya_signin&prevRID=63M6YCBVY9JQCK19KWN4&op'
           'enid.assoc_handle=usflex&openid.mode=checkid_setup&desktopBrowserWeblabT'
           'reatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http'
           '%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3'
           'A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


# Amazon Icon
driver.find_element(By.CSS_SELECTOR, '#a-page i.a-icon-logo')

# create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# your name box
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# email box
driver.find_element(By.CSS_SELECTOR, '#ap_email')

# password box
driver.find_element(By.CSS_SELECTOR, '#ap_password')

# text under the password box
driver.find_element(By.CSS_SELECTOR, '.a-row [aria-live="polite"] div.a-alert-content')

# re-enter password boc
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# create you account button
driver.find_element(By.CSS_SELECTOR, 'input#continue.a-button-input')

# condition of use
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='register_notification_condition_of_use?']")

# privacy notice
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='notification_privacy_notice']")

# sign in link
driver.find_element(By.CSS_SELECTOR, "a[href*= '/ap/signin?openid.pape.max_auth_age']")

