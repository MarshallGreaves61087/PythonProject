Feature: Patient Management using RDMS Database

Scenario: Load Patient in Database Table
	Given I Load for Patient Details to add in table
	
	|name	|age	|address		|email			|gender |
	|Rob	|25		|New Address 5	|rob@rob.com	|Male	|
	|Clint	|70		|New Address 6	|clint@clint.com|Male	|
	Then the patient data could be fetched from table 

Scenario: Fetch All Patient Details from the database Table
	Given Querying for Patient Data from Table
	Then to get the list of All Patients present in table	