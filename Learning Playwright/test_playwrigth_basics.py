from os import link

from playwright.sync_api import Page
from time import sleep

#This the steps to run it headless but --header allows me to visually see whats happening in the code
def test_launching_browser(page:Page):
    page.goto("https://www.amazon.com/")
    sleep(5)
    page.get_by_label("Search Amazon").fill("iphone") #going based on label name
    page.locator("#nav-search-submit-button").click()
    sleep(5)

    # going to cart using css selector
    # page.locator("#nav-cart-count-container .nav-cart-icon").click()
    # sleep(5)
    # locator by role
    # page.get_by_role("link", name= "Shop today's deals").click()
    # sleep(5)
    # Assertion
    # assert (page.get_by_text("Your Amazon Cart is empty")).is_visible()

# adding item to cart
def test_adding_item_to_cart(page:Page):
    # pre running
    page.goto("https://www.amazon.com/")
    sleep(5)
    page.get_by_label("Search Amazon").fill("iphone")  # going based on label name
    page.locator("#nav-search-submit-button").click()
    sleep(5)

    iphone14 = page.get_by_text("iPhone 14, 128GB, Midnight - Unlocked (Renewed)")
    iphone14.click()
    sleep(5)

# verify 2 items in cart
# def test_verify_title_is_correct(page:Page): # the filter feature don't work
#     # pre running
#     page.goto("https://www.amazon.com/")
#     sleep(5)
#     page.get_by_label("Search Amazon").fill("iphone")  # going based on label name
#     page.locator("#nav-search-submit-button").click()
#     sleep(5)
#
#     # iphone14 = page.get_by_text("iPhone 14, 128GB, Midnight - Unlocked (Renewed)")
#     # iphone14.click()
#     # sleep(5)
#
#     # title = page.locator("#title #productTitle").text_content() #to get the text content of the locator
#     # print(title)
#
#     title1= page.locator("div role").filter(has_text="iPhone 14, 128GB, Midnight - Unlocked (Renewed)") #another way of
#     #finding an item from a list using the item tag
#     title1.get_by_role("link", name="See options").click()
#
#     sleep(5)
#     prd_page_title = page.locator("#title #productTitle").text_content()
#     # assert title == "Apple iPhone 14, 128GB, Midnight - Unlocked (Renewed)"
#     assert prd_page_title == "Apple iPhone 14, 128GB, Midnight - Unlocked (Renewed)"
