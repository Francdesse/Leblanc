from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResults(Page):
    KEYWORD_SEARCH_IN_DOUBLE_QUOTE = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    CLICKING_ON_SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    APPLE_MOUSE = (By.XPATH, "//div[@data-asin='B09BRD98T4']"
                             "//div[@class='sg-row']//a[contains"
                             "(@href,'/Apple-Magic-Mouse-Wireless-Re') "
                             "and @class='a-link-normal s-underline-text"
                             " s-underline-link-text s-link-style a-text-normal']")
    def items_are_in_double_quotation(self):
        actual_text = self.find_element(*self.KEYWORD_SEARCH_IN_DOUBLE_QUOTE).text
        assert '"apple mouse"' in actual_text, f"Expected text not found, but found |{actual_text}|"
        #self.verify_element_text(self, expected_text='"apple mouse"', *self.KEYWORD_SEARCH_IN_DOUBLE_QUOTE)

    def user_click_on_search_button(self):
        self.click(*self.CLICKING_ON_SEARCH_BTN)
        self.click(*self.APPLE_MOUSE)

    def nav_amazon_page(self, product_id):
        self.open_url(url=f'https://www.amazon.com/gp/product/{product_id}/')

    def open_amazon_page(self):
        self.open_url(url=f'https://www.amazon.com/s?k=coffee')
