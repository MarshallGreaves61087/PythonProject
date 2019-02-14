import behave
from pip._vendor import requests
from nose.tools.trivial import ok_
from selenium import webdriver

@given("Request for all patients")
def fecth_patients_from_api(context):
    context.patients=requests.get("http://localhost:7770/api/patients/list").json()
    
@then("Have all the Patients from the API")
def check_all_patients_are_present(context):
    ok_(len(context.patients)>0,"Patients not Found")
        

@given("Request for all Report")
def fecth_reports_from_api(context):
    context.reports=requests.get("http://localhost:7770/api/reports/list").json()
    
@then("Have all the Report from the API")
def check_all_reports_are_present(context):
    ok_(len(context.reports)>0,"Reports not Found")
    
    
