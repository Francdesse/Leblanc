#check back with Carrerist on find elements and dropdown lists selections

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
driver.get("https://www.wikipedia.org")
sleep(2)

title = driver.title
print(title)

sleep(2)

#getting the dropdown list
search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchInput')))

sleep(2)

#printing the list of names from a dropdown list
option_list = driver.find_element(By.XPATH, '//*[@id="search-input"]/div[1]/div')
options = option_list.find_elements(By.TAG_NAME, 'option')
for option in options:
    print(option.text)

print('the length count of this list is ', len(options))


driver.quit()
