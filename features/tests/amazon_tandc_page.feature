# Created by belar at 3/8/2023
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can open and close Amazon Privacy Notice
   Given Open Amazon T&C page
   And Store original window
   When Click on Amazon Privacy Notice link
   And Switch to new window
   Then Verify Amazon Privacy Notice page is opened
   And Close page
   And Return to original window
