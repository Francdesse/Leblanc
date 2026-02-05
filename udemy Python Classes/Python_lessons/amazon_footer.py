from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC #allows you to use different wait locators
from time import sleep
from selenium.webdriver.common.by import By #allows you to use different locators by seperating them
from selenium.webdriver.common.keys import Keys #allows you to use keyboard shortcuts
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()
sleep(2)
driver.get("https://www.amazon.com")
sleep(2)

title = driver.title
print(title)

sleep(2)

# scrolling down the page to click on country
selecting_country = driver.find_element(by='css selector', value='#icp-touch-link-country.icp-button')
action = ActionChains(driver)
action.scroll_to_element(selecting_country).perform()
sleep(2)
selecting_country.click()

sleep(2)

#clicking the dropdown to select another country
action = ActionChains(driver)
country_dropdown = driver.find_element(by='css selector', value='.a-dropdown-container select#icp-dropdown')
action.click(country_dropdown)
sleep(2)

"""
WELP: I need to figure out how to use wait.until as ec so I can click on India
TO BE CONTINUED...


#india = driver.find_element(by='css selector', value='select#icp-dropdown, a#icp-dropdown_8.a-dropdown_link.icp-2 icp-flag-2 icp-flag-2-in')
selecting_india = driver. .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'select#icp-dropdown, a#icp-dropdown_8.a-dropdown_link.icp-2 icp-flag-2 icp-flag-2-in')))


"""

sleep(2)
#clicking on go to website
driver.find_element(by='css selector', value='#icp-save-button-announce').click()
sleep(2)

# switching window to select another country
original_window = driver.current_window_handle #1.store the original window handle
sleep(2)
all_windows = driver.window_handles#store all the window handles
driver.switch_to.window(driver.window_handles[1])#2.switch to the new window
sleep(2)

title = driver.title #get the title of the new window
print(title)


sleep(2)

driver.close()#3.close the new window
driver.switch_to.window(original_window)#4.switch back to the original window


