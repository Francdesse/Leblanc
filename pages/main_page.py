from pages.base_page import Page

class MainPage(Page):

    def open_amazon_page(self):
        self.open_url('https://www.amazon.com')