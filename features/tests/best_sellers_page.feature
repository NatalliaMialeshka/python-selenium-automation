# Created by belar at 2/22/2023
Feature: Best Sellers Page tests

 Scenario: User can open Best seller page and has the right amount of links
    Given Open Amazon page
    When Click on Best Sellers button
    Then Verify page has 5 links on the top


  Scenario: Bestsellers links could be opened
    Given Open Amazon page
    When Click on Best Sellers button
    Then User can click through links and verify them