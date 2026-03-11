from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver

from pages.base_page import Page
from time import sleep

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
    SEARCH_RESULT = (By.XPATH, "//h2//span[contains(text(), 'iphone')]")
    ITEM_RESULT = (By.CSS_SELECTOR, 'span[data-component-type="types-search-results"], div[class="a-section"] h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal')#filter down to 18 products (I need to bring it down to 15)
                   #'span[data-component-type="types-search-results"], div[class="a-section"] h2') #old path showing 20 items
    PRODUCT_TITLE = (By.ID, 'productTitle')
    CART = (By.ID, 'nav-cart-count-container')

    def user_nav_to_site(self):
        self.open_url("https://www.amazon.com")

    def user_search_item(self, searchText):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys(searchText)
        sleep(5)

    def user_click_search_btn(self):
        self.driver.find_element(*self.SEARCH_BTN).click()

    def search_item_is_shown(self, searchText):
        result = self.driver.find_element(*self.SEARCH_RESULT).text
        assert searchText in result, f"iphone is not in {result}"

    def selecting_third_item_from_search_result(self):
        result = self.driver.find_elements(*self.ITEM_RESULT)
        item_title = self.driver.find_elements(*self.ITEM_RESULT)[3].text
        print(f'Item title: {item_title}')
        self.driver.find_elements(*self.ITEM_RESULT)[3].click()
        sleep(15)

    def verify_each_links_are_clickable(self):
        result = self.driver.find_elements(*self.ITEM_RESULT)

        for item in range(2,len(result)):# its looping through all the items in the search result aka 17x
            try:
                element = result[item]

                self.driver.wait.until(EC.element_to_be_clickable(element))#checking if the element is clickable
                print(f'Item {item} is clickable')

            except TimeoutException:# the exceptions allow you to bypass the exception errors and continue otherwise the code will stop
                print(f'Item {item} is not clickable (timeout)')

            except StaleElementReferenceException:
                # DOM changed; re-find elements and retry once if you want
                print(f'Item {item} became stale (page changed)')


    def verify_print_out_each_item_title(self): #PRINTOUT THE TITLE FOR EACH PRODUCT ON THE HOMEPAGE
        result = self.driver.find_elements(*self.ITEM_RESULT)

        for item in range(3,len(result)):
            title = result[item].text.strip() #using RESULT that is set outside the loop, so no need to use .find element.text
            print(item, title)

        # result = self.driver.find_elements(*self.ITEM_RESULT) #also works
        #
        # for item in range(3, len(result)):  # its looping through all the items in the search result aka 17x
        #     try:
        #         title = result[item].text.strip
        #         print(f'Product:  {title}')

    def verify_search_title_the_same_as_product_title(self):
        result = self.driver.find_elements(*self.ITEM_RESULT)

        for item in range(3, len(result)):
            search_title = result[item].text.strip()  # using RESULT that is set outside the loop, so no need to use .find element.text
            print(item, search_title)

            result[item].click() #doing title=... made it stale, thats why it didnt work before

            self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLE))

            product_title = self.driver.find_element(*self.PRODUCT_TITLE).text

            print(f'Product title: {product_title}')
            assert search_title == product_title, f'Product title is not the same as {search_title}'

            self.driver.back()

            # Wait until you're really back on results page before next loop
            self.wait.until(EC.presence_of_all_elements_located(self.ITEM_RESULT))

    def user_clicks_on_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.CART)).click()
