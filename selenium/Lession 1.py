from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/ref=nav_bb_logo")

driver.maximize_window()
search_bar = (By.ID, "twotabsearchtextbox")
search_btn = (By.ID, "nav-search-submit-button")



driver.find_element(*search_bar).send_keys("protein bars")
driver.find_element(*search_btn).click()

wait = WebDriverWait(driver, 10)

"""
    Handling dropdown list
"""
