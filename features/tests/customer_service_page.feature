Feature: Verify the list of boards of both customer service and all help topics
  Scenario: verify that user sees the welcome message on the page
    Given navigate to the customer service page
    Then verify user sees Welcome to Amazon customer service


  Scenario: verify that there are 10 links under customer service
    Given navigate to the customer service page
    Then verify that there are 10 links on the page

  Scenario: verify that the search bar is present
    Given navigate to the customer service page
    Then verify the search bar title is present
    Then verify the search bar is present
    Then verify that user sees All help topics


  Scenario: verify that users sees 11 links under help topics
    Given navigate to the customer service page
    Then verify that user sees 11 links under help topics