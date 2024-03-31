# Created by francdelmonde at 3/31/24
Feature: Target search features
  # Enter feature description here

  Scenario: verify that 5 elements are present
    Given user navigate to https://www.target.com/circle
    Then  verify there are 5 elements present

  Scenario: verify elements on the page are displayed
    Given user navigates to https://help.target.com/help
    Then  verify all elements are present