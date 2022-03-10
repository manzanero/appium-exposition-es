@demo2 @android_driver
Feature: Contact Manager

 Scenario: Add a contact
   Given the user access list of contacts
   When the user press "Add Contact"
   And the user enters "Contact Name"
   And the user enters "Contact Phone"
   And the user press "Save"
   Then the contact appears in the list