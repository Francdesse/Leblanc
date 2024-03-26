# Created by francdelmonde at 3/25/24
Feature: amazon search feature
  # Enter feature description here

  Scenario: user is able to search product
    Given user launch amazon site
    When user search for coffee
    And user clicks on search button
    Then verify that user sees "coffee"