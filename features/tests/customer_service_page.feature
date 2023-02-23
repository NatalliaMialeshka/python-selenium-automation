# Created by belar at 2/22/2023
Feature: Customer Service page tests
  # Enter feature description here

  Scenario: User can open Customer Service page and all elements are there
    Given Open Amazon page
    When Click on Customer Service button
    Then Verify main header presents
    Then Verify 9 links are presented on the page
    Then Verify secondary header presented
    Then Verify search bar is presented
    Then Verify the topic title is presented
    Then Verify there are 11 help links
