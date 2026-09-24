from playwright.sync_api import Page
from time import sleep

#This the steps to run it headless but --header allows me to visually see whats happening in the code
def test_launching_browser(page:Page):
    page.goto("https://www.amazon.com/")
    sleep(5)
    page.get_by_label("Search Amazon").fill("iphone")
    page.locator("#nav-search-submit-button").click()
    sleep(5)