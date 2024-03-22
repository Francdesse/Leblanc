from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()

service=Service(driver_path)
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")

