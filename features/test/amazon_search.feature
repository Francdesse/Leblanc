Feature: testing search

    Scenario: 1
        Given user go to amazon
        When search for "iphone"
        Then iphone is showned in the search HRESULT
