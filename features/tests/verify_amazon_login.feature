# Created by francdelmonde at 5/7/23
Feature: Verify the sign in page opens after user clicks on orders


  Scenario: User gets the login page
    Given Open Amazon page
    When Clicks on orders
    Then Verify user is taken to the sign in page

  Scenario: verify that cart is empty
    Given Open Amazon page
    When click on cart
    Then cart is empty message

  Scenario: verify the item is shown in ""
    Given Open Amazon page
    When search for an apple mouse
    When click search button
    Then verify item is in double quotes


  Scenario: add item to cart and  verify that the "added to cart" message popped up
    Given Open Amazon page
    When Search for an apple mouse
    When click on the first result
    When store item title
    When click on add to cart
    When decline coverage protection
    Then verify added to cart message


  Scenario: add item to cart and  verify the item is in cart
    Given Open Amazon page
    When Search for an apple mouse
    When click on the first result
    When store item title
    When click on add to cart
    When decline coverage protection
    When click on cart
    Then verify apple mouse is in cart


  Scenario: add item to cart and  verify the item is in cart 2
    Given Open Amazon page
    When Search for an apple mouse
    When click on the first result
    When click on add to cart
    When decline coverage protection
    When click on cart
    Then verify that cart has 1 item

  Scenario: generate a loop to loop through each items
    Given user navigate to product page B07BJKRR25
    Then verify all items are functional

  Scenario: generate a loop to verify product has an image and product name
    Given user navigate to product page
    Then verify all product names are present & verify all product image are present


  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And close Privacy notice page
    And switch back to original

  Scenario: Go to best seller's page and verify the best seller menu open to the right pages
    Given Open Amazon page
    When user clicks on best sellers
    Then verify each pages that each pases open to the right page from the menu


#  steps:
#  1-  go to amazon>>add search item>> click search>>verify that its shows item search in ""
  #2-  click on an item>> add it to cart>> verify its in cart