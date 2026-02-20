from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given('user go to amazon')
def step_impl(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.amazon.com")
    sleep(5)

@when('search for "iphone"')
def step_impl(self):
    self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphone")

@when('clicks on search button')
def user_clicks_on_search_btn(self):
    self.driver.find_element(By.ID, "nav-search-submit-button").click()
    sleep(5)

@then('iphone is showned in the search result')
def verify_search_item(self):
    search_result = self.driver.find_element(By.XPATH, "//h2//span[contains(text(), 'iphone')]").text
    assert 'iphone' in search_result, f"iphone is not in {search_result}"