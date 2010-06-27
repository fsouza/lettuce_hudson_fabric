Feature: Students registry
    In order to manage the school
    As a school employee
    I want to register the school's students

    Scenario: Saving a simple student
        Given that I am logged in the system
        When I navigate to the new student page
        And fill the name field with "Francisco Souza"
        And save this student with the code "1"
        Then I should be redirect to the page of student "1"
        And the page title should contains "Francisco Souza"
