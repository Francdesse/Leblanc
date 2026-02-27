from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ProductPage(Page):
    PRODUCT_TITLE = (By.ID, 'productTitle')


    def verify_that_product_name_is_the_same_as_product_title(self):
        product_title = self.find_element(*self.PRODUCT_TITLE).text
        print(f'Product title: {product_title}')
