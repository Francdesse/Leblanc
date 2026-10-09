from playwright.sync_api import Playwright, Page
from time import sleep

#rahulshetty33@gmail.com
#Password123$$
#log in process
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
        # adding Item to cart
    #grabbing the text
    item_tile = page.get_by_text("ADIDAS ORIGINAL").text_content()
    page.locator('#products > div.container > div.row > div:nth-child(1) > div > div > button.btn.w-10.rounded').click()
    sleep(5)
    page.locator("button.btn-custom[routerlink='/dashboard/cart']").click()
    sleep(2)
    cart_item = page.locator(".cartSection h3").text_content()
    assert item_tile == cart_item
    sleep(2)

    #checking out
    page.get_by_role("button", name="Checkout").click()
    sleep(2)
    page.locator('.form-group .input.txt.text-validated').fill("United States")
    # page.get_by_role("button", name="United States").click()
    # sleep(2)
    page.locator('.btnn.action__submit.ng-star-inserted').click()
    sleep(2)

    #order confirmation
    order_confirmation = page.get_by_text("Thank you, your order has been placed successfully.")
    assert order_confirmation
    sleep(5)