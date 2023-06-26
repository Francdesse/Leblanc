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
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.sg-col-inner [data-component-type= "s-search-result"]')
    ITEM_TITLES = (By.XPATH, ".//span[@class='a-size-base-plus a-color-base a-text-normal']")
    IMAGE = (By.XPATH, "//img[@class='s-image']")
    VIDEO_GAME = (By.CSS_SELECTOR, '[aria-label="Video Games"]')

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

    def img_and_work_present(self):
        products = self.driver.find_elements(*self.SEARCH_RESULTS)

        for product in products:
            title = product.find_element(*self.ITEM_TITLES).text
            print(title)
            assert title, "title is missing"
            assert product.find_element(*self.IMAGE).is_displayed(), "image is missing"


    def user_sees_video_games(self):
        self.verify_element_text('Video Games', *self.VIDEO_GAME)
