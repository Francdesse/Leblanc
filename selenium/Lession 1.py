from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

driver = webdriver.Chrome()
driver.get("https://google.com")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#APjFqb").send_keys("tesla model s")
#driver.implicitly_wait(3)
test = wait.until(EC.element_to_be_clickable(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]"))

#sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
driver.implicitly_wait(5)

"""
    Make this work. To be continue

"""