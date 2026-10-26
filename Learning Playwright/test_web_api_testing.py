from playwright.sync_api import Playwright, Page, expect
from pageObjects.login import LoginPage #connecting the login page to the login test section
from pageObjects.dashboard import DashboardPage
from pageObjects.cart import CartPage
from utils.apiBase import APIUtils
from time import sleep

#rahulshetty33@gmail.com
#Password123$$
#log in process
def test_start_page(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #calling create first order api call
    api_utils = APIUtils()
    order_id = api_utils.create_first_order(playwright)


    #login to main page
    loginPage = LoginPage(page)
    loginPage.UrlNavigate()
    dashboardPage = loginPage.login()

    # adding Item to cart
    #grabbing the text
    cartpage = dashboardPage.addingItemtoCart()

    #checking out
    cartpage.checkingOutitem()

    #order confirmation
    # cartPage.orderConfirmationMsg()

    #verify order id







#     col = page.locator("th").count()
#
#     for i in range(col):
#         if page.locator("th").nth(i).text_content() == "Order Id":
#
#             order_name = page.locator("tr").filter(has_text="ADIDAS ORIGINAL")
#             expect(order_name.locator("td").filter(has_text="$ 11500"))
#
#             break
#
# #HELPPPPPP, QUESTION: why not go into the table to find the order id???