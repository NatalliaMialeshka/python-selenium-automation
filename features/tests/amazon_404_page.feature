# Created by belar at 3/8/2023
Feature: Tests for 404 page

  Scenario: User is able to navigate to amazon blog from 404 page
    Given Open Amazon product B07NF5WGQ1111111 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close page
    And Return to original window