from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.get("https://google.com")

driver.maximize_window()

driver.find_element(By.css_selector("#APjFqb")).click()