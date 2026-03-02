from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
    SEARCH_RESULT = (By.XPATH, "//h2//span[contains(text(), 'iphone')]")
    ITEM_RESULT = (By.CSS_SELECTOR, 'span[data-component-type="types-search-results"], div[class="a-section"] h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal')#filter down to 18 products (I need to bring it down to 15)
                   #'span[data-component-type="types-search-results"], div[class="a-section"] h2') #old path showing 20 items



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
        result = self.driver.find_elements(*self.ITEM_RESULT).count
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


    def verify_print_out_each_item_title(self): #I NEED TO FIGURE OUT HOW TO PRINTOUT THE TITLE
        # result = self.driver.find_elements(*self.ITEM_RESULT)
        # for item in range(3,len(result)):
        #     title = self.driver.find_element(*self.ITEM_RESULT).text
        #      #result[item].text) #how do I get the text to print out?
        #     print(item, result)

        result = self.driver.find_elements(*self.ITEM_RESULT)

        for item in range(3, len(result)):  # its looping through all the items in the search result aka 17x
            try:
                element = result[item]
                  # checking if the element is clickable
                print(f'Item {element} is clickable')

            except TimeoutException:  # the exceptions allow you to bypass the exception errors and continue otherwise the code will stop
                print(f'Item {element} is not clickable (timeout)')

            except StaleElementReferenceException:
                # DOM changed; re-find elements and retry once if you want
                print(f'Item {element} became stale (page changed)')
