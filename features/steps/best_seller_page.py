from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BEST_SELLER_TAB_LINKS = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')

@given('user navigate to the best seller page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')




@then('verify user counts 5 links')
def user_counts_5_links(context):
    link_counts = len(context.driver.find_elements(*BEST_SELLER_TAB_LINKS))
    assert link_counts > 3, f'Error Expected to be greater then 3 but got {link_counts}'
    print(link_counts, (context.driver.find_elements(*BEST_SELLER_TAB_LINKS)))