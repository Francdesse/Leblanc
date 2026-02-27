from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
    SEARCH_RESULT = (By.XPATH, "//h2//span[contains(text(), 'iphone')]")
    ITEM_RESULT = (By.CSS_SELECTOR, 'span[data-component-type="types-search-results"], div[class="a-section"] h2')



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
        item_title = self.driver.find_elements(*self.ITEM_RESULT)[5].text
        print(f'Item title: {item_title}')
        self.driver.find_elements(*self.ITEM_RESULT)[5].click()
        sleep(15)
