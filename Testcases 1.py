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


# open the url
driver.get('https://www.amazon.com')

# click on orders
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_orders_first')]").click()

# Verify the sign in page open

expected_result = "Sign in"
actual_result1 = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result == actual_result1

print('sign in pass')



driver.quit()