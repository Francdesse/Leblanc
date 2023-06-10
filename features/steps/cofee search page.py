from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS = (By.CSS_SELECTOR, '.sg-col-inner [data-component-type= "s-search-result"]')
ITEM_TITLES = (By.XPATH, ".//span[@class='a-size-base-plus a-color-base a-text-normal']")
IMAGE = (By.XPATH, "//img[@class='s-image']")

@given('user navigate to product page')
def open_amazon_page(context):
    context.app.search_results.open_amazon_page()

@then ('verify all product names are present & verify all product image are present')
def img_and_work_present(context):
    products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in products:
        title= product.find_element(*ITEM_TITLES).text
        print(title)
        assert title, "title is missing"
        assert product.find_element(*IMAGE).is_displayed(), "image is missing"