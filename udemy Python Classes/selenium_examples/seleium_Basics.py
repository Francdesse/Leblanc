from selenium import webdriver
from time import sleep

driver = webdriver.Safari()

# options = webdriver.SafariOptions()
# driver = webdriver.Safari(options=options) #keep in the background for now


driver.maximize_window()
sleep(2)
driver.get("https://www.google.com/")
sleep(2)

title = driver.title
print(title)

sleep(2)

driver.find_element(by='xpath', value='//*[@id="APjFqb"]').send_keys('Selenium')


driver.quit()
