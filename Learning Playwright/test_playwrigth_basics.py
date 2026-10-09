from os import link

from playwright.sync_api import Page, expect
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

# working with a new window
def test_new_window_popup(page:Page):
    page.goto("https://www.amazon.com/")
    sleep(2)
    page.locator("#icp-touch-link-country .icp-color-base").click()
    sleep(2)
    page.get_by_role("button", name="Go to website").click()

    with page.expect_popup() as new_page_info:
        childPage = new_page_info.value
        recommendation_text = childPage.locator('.rhf-sign-in-title').text_content()
        assert "personalized" in recommendation_text
        childPage.close()
        sleep(5)

# going to the sign in page using 'Sign in' popup box link
def test_sign_in_page(page:Page):
    page.goto("https://www.amazon.com/")
    sleep(2)
    page.locator('#nav-signin-tooltip .nav-action-inner').click()
    sleep(2)
    title = page.locator("#claim-collection-container h1").text_content()
    answer = title.split("or")
    assert "Sign in" in answer[0]

#working with tables
#goal is to assert the price is equal to 37
#identify the price colunm
#identify the rice row
#extract the price of the rice
def test_verify_price_of_rice(page:Page):
    page.goto('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    sleep(2)

    # for i in range(page.locator("th").count()):
    #     if page.locator("th").nth(i).filter(has_text="Price").count() > 0:
    #         col_value = i;
    #         print(f'col_value: {col_value}')
    #         break
    #
    # riceRow = page.locator("tr").filter(has_text="Rice")
    # expect(riceRow.locator("td").nth(col_value)).to_have_text("39")

    col= page.locator("th").count() #the 3 columns

    for i in range(col):
         if page.locator("th").nth(i).text_content() == "Price" and page.locator("th").nth(i).count() >0:
        # if page.locator("th").nth(i).filter(has_text="Price").count() > 0:#focus only on price column and nth(i) allows
            #me to access the th index(this is a simpler way to write line 107)
            col_value = i
            print(f'col_value: {col_value}')
            item_name = page.locator("tr").filter(has_text="Rice")
            expect(item_name.locator("td").nth(col_value)).to_have_text("37")
            break


#     item_name = page.locator("tr").filter(has_text="Rice")
#     expect(item_name.locator("td").nth(col_value)).to_have_text("37")
# # Question: can I do everything inside the if statement then break???

# #working with tables
# #goal is to assert the price is equal to 34
# #identify the price colunm
# #identify the potato row
# #extract the price of the potato
# def test_verify_price_of_rice(page:Page):
#     page.goto('https://rahulshettyacademy.com/seleniumPractise/#/offers')
#     sleep(2)
#
#     col= page.locator("th").count() #the 3 columns
#
#     for i in range(col):
#          if page.locator("th").nth(i).text_content() == "Price" and page.locator("th").nth(i).count() >0:
#         # if page.locator("th").nth(i).filter(has_text="Price").count() > 0:#focus only on price column and nth(i) allows
#             #me to access the th index(this is a simpler way to write line 107)
#             col_value = i
#             print(f'col_value: {col_value}')
#             item_name = page.locator("tr").filter(has_text="Potato")
#             expect(item_name.locator("td").nth(col_value)).to_have_text("34")
#             break


#working with tables
#goal is to assert the price is equal to 34
#identify the Discount price colunm
#identify the potato row
#extract the discount price of the potato
def test_verify_price_of_rice(page:Page):
    page.goto('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    sleep(2)

    col= page.locator("th").count() #the 3 columns

    for i in range(col):
         if page.locator("th").nth(i).text_content() == "Discount price" and page.locator("th").nth(i).count() >0:
        # if page.locator("th").nth(i).filter(has_text="Price").count() > 0:#focus only on price column and nth(i) allows
            #me to access the th index(this is a simpler way to write line 107)
            col_value = i
            print(f'col_value: {col_value}')
            item_name = page.locator("tr").filter(has_text="Potato")
            expect(item_name.locator("td").nth(col_value)).to_have_text("22")#expect 22
            break
