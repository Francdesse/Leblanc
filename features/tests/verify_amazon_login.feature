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
    When click on add to cart
    When decline coverage protection
    Then verify added to cart message


  Scenario: add item to cart and  verify the item is in cart
    Given Open Amazon page
    When Search for an apple mouse
    When click on the first result
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



#  steps:
#  1-  go to amazon>>add search item>> click search>>verify that its shows item search in ""
  #2-  click on an item>> add it to cart>> verify its in cart