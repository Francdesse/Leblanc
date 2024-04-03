# Created by francdelmonde at 3/25/24
Feature: amazon search feature
  # Enter feature description here

  Scenario: user is able to search product
    Given user launch amazon site
    When user search for coffee
    And user clicks on search button
    Then verify that user sees "coffee"

  Scenario: verify the cart empty message
    Given user launch amazon site
    When user clicks on cart
    Then verify Your Amazon Cart is empty message

  Scenario: verify that user sees the login popup login box
    Given user launch amazon site
    When verify that the login popup box comes up
    When user click on signin popup
    Then verify that user is in the sign in page
