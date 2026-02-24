from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")

sleep(3)
driver.find_element(by='xpath', value="//input[@id='twotabsearchtextbox']").send_keys('iphone')
sleep(2)
driver.quit()

