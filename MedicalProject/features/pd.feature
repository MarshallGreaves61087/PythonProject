Feature: Patient Management using RDMS Database

Scenario: Load Patient in Database Table
	Given Request for all patients
	Then Have all the Patients from the API
	
Scenario: Fetch All Patient Details from the database Table
	Given Querying for Patient Data from Table
	|name	|age	|address		|email			|gender |
	|Rob	|25		|New Address 5	|rob@rob.com	|Male	|
	|Clint	|70		|New Address 6	|clint@clint.com|Male	|
	Then increases Patient Count from API	