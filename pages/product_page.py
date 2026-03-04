from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ProductPage(Page):
    PRODUCT_TITLE = (By.ID, 'productTitle')


    def verify_that_iphone_is_in_the_title(self):
        product_title = self.find_element(*self.PRODUCT_TITLE).text
        print(f'Product title: {product_title}')
        assert 'iPhone 12' in product_title, f'Product title is not the same as {product_title}'
        #assert item_title == product_title, f'Product title is not the same as {item_title}'