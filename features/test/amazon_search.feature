Feature: testing search

    Scenario: 1
        Given user go to amazon
        When search for iphone
        And clicks on search button
        Then iphone is showned in the search result
