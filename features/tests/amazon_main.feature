# Created by belar at 2/21/2023
Feature: Amazon main page tests

  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify hamburger menu icon present
    When Click on ham menu

  Scenario: Footer and header has correct amount of links
    Given Open amazon page
    Then Verify that footer has 36 links
    Then Verify that header has 29 links

  Scenario: User can open Best seller page and has the right amount of links
    Given Open Amazon page
    When Click on Best Sellers button
    Then Verify page has 5 links on the top


  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present


  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias baby-products
    When Input text toys
    When Click on search button
    Then Verify baby-products department is selected