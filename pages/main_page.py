from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')

    def user_nav_to_site(self):
        self.open_url("https://www.amazon.com")

    def user_search_item(self, searchText):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys(searchText)
        sleep(5)