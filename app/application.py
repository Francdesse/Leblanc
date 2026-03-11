# The application file call and connects all the pages together
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages. cart_page import CartPage
# from pages.model3_demo_page import MODEL3DEMOPAGE
# from pages.sign_in_page import SignInPage



class Application:

    def __init__(self, driver):
        self.driver = driver

        #self.header_page =  Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        # self.model3_demo_page = MODEL3DEMOPAGE(self.driver)
        # self.sign_in_page = SignInPage(self.driver)