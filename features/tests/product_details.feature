# Created by belar at 3/3/2023
Feature: Tests for product page
  # Enter feature description here

  Scenario: User can select colors
  Given Open Amazon product B09D2SQNWD page
  Then Verify user can click through colors
    # Enter steps here

  Scenario: User can select different colors of Men Jeans
    Given Open Amazon product B07BJL37GD page
    Then Verify user can select different colors
