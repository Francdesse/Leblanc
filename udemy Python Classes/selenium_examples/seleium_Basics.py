from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC #allows you to use different wait locators
from time import sleep
from selenium.webdriver.common.by import By #allows you to use different locators by seperating them
from selenium.webdriver.common.keys import Keys #allows you to use keyboard shortcuts
from selenium.webdriver.support.wait import WebDriverWait

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

search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
search_box.send_keys('Selenium' + Keys.ENTER)

sleep(2)
# driver.find_element(by='xpath', value='//*[@id="APjFqb"]').send_keys('Selenium')



driver.quit()
