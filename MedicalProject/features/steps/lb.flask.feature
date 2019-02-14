Feature: Lab_Manager Management using Flask

Background: Start the Flask

Scenario: Get the Lab Manager from API
	Given Request for All Lab_Managers
	Then have all lab_managers available from application
	
Scenario: Add Lab_Manager Details using API
	Given a set lb for API
	|lab_manager_id	|name	|location	|test		|result			|
	|1				|Jimmy	|London		|Neck exam	|All clear		|
	Then increase the Lab_Manager Count from API