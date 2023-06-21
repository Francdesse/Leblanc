from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGNIN_PAGE = (By.XPATH, "//h1[@class='a-spacing-small']")
    def load_sign_in_page(self):
        self.verify_element_text('Sign in', *self.SIGNIN_PAGE)