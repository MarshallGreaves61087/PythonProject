Feature: Report Management using RDMS Database

Scenario: Load Report in Database Table
	Given I Load for Report Details to add in table
	
	|title					|related_illness	|date		|notes				|prescription 	|
	|Doctors Appointment	|Chest Infection	|13/02/2019	|Breathing problems	|Anti-Biotics	|
	|Rushed to hospital		|Heart Attack		|14/02/2019	|Heart Attacks		|Nitroglycerin	|				
	Then the report data could be fetched from table 

Scenario: Fetch All Report Details from the database Table
	Given Querying for Report Data from Table
	Then to get the list of All Reports present in table	