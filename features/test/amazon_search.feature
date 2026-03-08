Feature: testing search

    Scenario: 1
        Given user go to amazon
        When search for iphone
        And clicks on search button
        Then iphone is showned in the search result

    Scenario: selecting an iphone from search result
        Given user go to amazon
        When search for iphone
        And clicks on search button
        And selecting third item from search result
        Then verify that iphone is in the title

   Scenario: Checking if each products are clickable
        Given user go to amazon
        When search for iphone
        And clicks on search button
        Then verify each links are clickable

   Scenario: Getting the title for each item
        Given user go to amazon
        When search for iphone
        And clicks on search button
        Then verify/print out each item title

  Scenario: comparing the search title to product title
        Given user go to amazon
        When search for iphone
        And clicks on search button
        Then verify search title the same as product title

  Scenario: verify user is able to add item to cart
  Scenario: verify the item added to cart has the same title as search item
  Scenario: verify that when an item is added to cart 1 is shown on cart
  Scenario: verify that when user clicks on cart, it shows empty cart