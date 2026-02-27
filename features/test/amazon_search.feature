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
        Then verify that product name is the same as product title

