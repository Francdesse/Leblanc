#check back with Carrerist on find elements and dropdown lists selections
# 26254624 | Practicing Xpath variations

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC #allows you to use different wait locators
from time import sleep
from selenium.webdriver.common.by import By #allows you to use different locators by seperating them
from selenium.webdriver.common.keys import Keys #allows you to use keyboard shortcuts
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

# options = webdriver.SafariOptions()
# driver = webdriver.Safari(options=options) #keep in the background for now


driver.maximize_window()
sleep(2)
driver.get("https://www.amazon.com")
sleep(2)

title = driver.title
print(title)
# # finding element using id
# driver.find_element(by='xpath', value="//input[@id='twotabsearchtextbox']").send_keys('iphone')
# sleep(2)
#
# # finding element using and
# driver.find_element(by='xpath', value='//input[@id="nav-search-submit-button" and @type="submit"]').click()
# sleep(2)
#
# # finding element using contains
# result_output = driver.find_element(by='xpath', value='//h2//span[contains(text(), "iphone")]').text
# assert 'iphone' in result_output
# sleep(2)

# running everything with css selectors
driver.find_element(by='css selector', value='#twotabsearchtextbox').send_keys('iphone')

sleep(2)

driver.find_element(by='css selector', value='span .nav-input.nav-progressive-attribute').click()

sleep(4)

driver.find_element(by='xpath',  value='//div//span[contains(text(), "Apple iPhone 14 (Renewed), 128GB, Mi")]').click()
sleep(2)

get_title = driver.find_element(by='css selector', value='#title #productTitle').text
assert 'Apple iPhone 14 (Renewed), 128GB, Midnight' in get_title, f'title is not correct, \
the correct title is {get_title}'

# scrolling down the page to click on contact us
# contact_us = driver.find_element(by='xpath', value="//div//a[contains(text(), 'contact us')]")
# action = ActionChains(driver)
# action.scroll_to_element(contact_us).perform()
# sleep(2)
# contact_us.click()

sleep(2)
driver.quit()
