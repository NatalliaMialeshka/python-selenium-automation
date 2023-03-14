# Created by belar at 2/18/2023
Feature: Amazon search tests


  Scenario Outline: User can search for coffee on Amazon
    Given Open Amazon page
    When Input text <search_word>
    And Click on search button
    Then Verify that text <search_result> is shown
    Examples:
    |search_word  |search_result  |
    |coffee       |"coffee"       |
    |table        |"table"        |
    |mug          |"mug"          |


  Scenario: User can search for a table on Amazon
    Given Open Amazon page
    When Input text table
    When Click on search button
    Then Verify that text "table" is shown
#
#  Scenario: User can search for a mug on Amazon
#    Given Open Amazon page
#    When Input text mug
#    When Click on search button
#    Then Verify that text "mug" is shown




  Scenario: Verify that product on Amazon search results has name and image
    Given Open Amazon page
    When Input text watches
    And Click on search button
    Then Verify that text "watches" is shown
    And Verify that every product has name and image


#  Scenario: User can click on a hamburger menu
#    Given Open Amazon page
#    Then Verify hamburger menu icon present
#
#  Scenario: Footer has correct amount of links
#    Given Open amazon page
#    Then Verify that footer has 38 links