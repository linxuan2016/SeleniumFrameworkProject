Feature: Login
    As a normal user
    I want to do login
    In order to use the scrumboard

    @login
    Scenario: Login
        Given I navigate to the login page
        When I login with user "linxuan"
        And I click on the submit button
        Then I am directed to the scrumboard page


