from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_VARIATIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
@given('user navigate to product page {product_id}')
def nav_amazon_page(context, product_id):
    #context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')
    context.app.search_results.nav_amazon_page(product_id)


@then ('verify all items are functional')
def items_are_functional(context):
    context.app.product_page.items_are_functional()
    # expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed']
    # actual_colors = []
    #
    # # colors = context.driver.find_elements(*COLOR_VARIATIONS)
    #
    # for i in range(5):
    #     color = context.driver.find_elements(*COLOR_VARIATIONS)[i]
    #     color.click()
    #     current_color = context.driver.find_element(*CURRENT_COLOR).text
    #     actual_colors += [current_color]
    #
    #     # image = context.driver.find_elements(*YOUR_LOCATOR)[i]
    #     # image.is_displayed()
    #
    # assert expected_colors == actual_colors, \
    #    f'Expected colors {expected_colors} did not match actual {actual_colors}'
    #




