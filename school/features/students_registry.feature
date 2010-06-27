Feature: Students registry
    In order to manage the school
    As a school employee
    I want to register the school's students

    Scenario: Registering a student
        Given there are the following users registered in the system
            | names          |
            | Mary Thompson  |
        When I navigate to the new student page
        And fill the name field with "Francisco Souza"
        And save this student with the code "1"
        Then I should be redirect to the page of student "1"
        And the page title should contains "Francisco Souza"
