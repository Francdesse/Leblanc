from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()

service=Service(driver_path)
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.com/")

driver.find_element(By.CSS_SELECTOR,'.nav-input[placeholder="Search Amazon"]').send_keys("apple")
driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button[value="Go"]').click()

expected = '"apple"'
actual = driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text
assert expected == actual, f"Expected {expected} is not the same as {actual} "
print('Test Complete')
