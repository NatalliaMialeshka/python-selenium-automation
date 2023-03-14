# Created by belar at 2/18/2023
Feature: Amazon cart tests

  Scenario:  'Your Amazon Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart
    Then Verify that text "Your Amazon cart is empty" is shown


  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text melatonin
    When Click on search button
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)