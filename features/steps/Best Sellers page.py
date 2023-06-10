from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

BEST_SELLER_LINK = (By.CSS_SELECTOR, '[data-csa-c-content-id="nav_cs_bestsellers"]')
BEST_SELLER_LINKS = (By.CSS_SELECTOR, 'ul li a[href*="ref=zg"]')
                     #".//div[@class= '_p13n-zg-nav-tab-all_style_zg-tabs-li-selected-div__3tHnP']")
MENUE_TITLE_DESCR = (By.CSS_SELECTOR, '#zg_banner_text')


@when('user clicks on best sellers')
def user_clicks_and_open_best_seller_page(context):
    # context.driver.wait.until(EC.element_to_be_clickable(BEST_SELLER_LINK))
    # context.driver.find_element(*BEST_SELLER_LINK).click()
    context.app.header_page.user_clicks_and_open_best_seller_page()



@then('verify each pages that each pases open to the right page from the menu')
def verify_each_windows_with_its_title(context):
    expected_titles = ["Amazon Best Sellers", "Amazon Hot New Releases", "Amazon Movers & Shakers",
                       "Amazon Most Wished For", "Amazon Gift Ideas"]
    menues = context.driver.find_elements(*BEST_SELLER_LINKS)
    number_of_links = len(menues)


    for i in range(number_of_links):
        menu_element = context.driver.find_elements(*BEST_SELLER_LINKS)[i]
        menu_element.click()
        menue_title_descri = context.driver.find_element(*MENUE_TITLE_DESCR).text
        print(menue_title_descri)
        assert menue_title_descri in expected_titles, 'title description is missing'



