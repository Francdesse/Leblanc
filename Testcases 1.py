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

Expected_result = "Sign in"
Actual_result1 = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert Expected_result == Actual_result1

print('sign in pass')

# Verity user is able to contunue to the next page with a valid email
driver.find_element(By.ID, 'ap_email').send_keys('francyoudesse@icloud.com')
driver.find_element(By.ID, 'continue').click()

Expected_result2= 'francyoudesse@icloud.com'
Actual_result2= driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']//span[text()='francyoudesse@icloud.com']").text
assert Expected_result2 == Actual_result2

print('Continue is clickable')

driver.quit()