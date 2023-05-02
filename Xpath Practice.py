# 5/1/23

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
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')


# find Amazon logo element
driver.find_element(By.XPATH, "//i[@class= 'a-icon a-icon-logo']")

# find Continue button element
driver.find_element(By.XPATH, "//input[@id= 'continue']")

# find need help link element
driver.find_element(By.XPATH, "//span[@class= 'a-expander-prompt']")

# find forgot password link element
driver.find_element(By.XPATH, "//a[@id= 'auth-fpp-link-bottom']")

# find Other issues with Sign-In link element
driver.find_element(By.XPATH, "//a[contains(@href, 'customer/account-issue')  and @id= 'ap-other-signin-issues-link']")

# find create your amazon account button element
driver.find_element(By.XPATH, "//a[@id= 'createAccountSubmit']")

# find conditions of use link element
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# find privacy notice link element
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

