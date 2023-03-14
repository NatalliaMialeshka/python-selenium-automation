# Created by belar at 3/3/2023
Feature: Amazon Sign in tests

  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens


  Scenario: Sign in popup is visible for a few sec
    Given Open Amazon page
    Then Verify Sign in popup shown
    When Wait for 8 sec
    Then Verify Sign in popup shown
    Then Verify Sign in popup disappears


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page opens

