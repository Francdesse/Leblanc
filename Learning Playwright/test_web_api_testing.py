from playwright.sync_api import Playwright
from time import sleep

#rahulshetty33@gmail.com
#Password123$$
def test_start_page(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #login to main page
    page.goto("https://rahulshettyacademy.com/client/")
    sleep(3)
    page.locator('#userEmail').fill("rahulshetty33@gmail.com")
    page.locator("#userPassword").fill("Password123$$")
    page.get_by_role("button", name="Login").click()
    sleep(3)

