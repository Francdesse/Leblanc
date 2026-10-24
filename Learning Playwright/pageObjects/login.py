from .dashboard import DashboardPage
from time import sleep

class LoginPage:

    def __init__(self,page):
        self.page = page

    def UrlNavigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self):
        self.page.locator('#userEmail').fill("rahulshetty33@gmail.com")
        self.page.locator("#userPassword").fill("Password123$$")
        self.page.get_by_role("button", name="Login").click()
        sleep(3)
        dashboardPage = DashboardPage(self.page)
        return dashboardPage