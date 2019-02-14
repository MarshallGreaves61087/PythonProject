import behave
from pip._vendor import requests
from nose.tools.trivial import ok_
from selenium import webdriver

@given("Request for all patients")
def fecth_patients_from_api(context):
    context.patients=requests.get("localhost:7700/api/patients/list").json()
    
@then("Have all the Patients from the API")
def check_all_patients_are_present(context):
    ok_(len(context.patients)>0,"Patients not Found")
    
@given("Querying for Patient Data from Table")
def post_patients_to_api(context):
    context.currentCount = len(requests.get(
        "localhost:7700/api/patients/list").json())
    for row in context.table:
        new_patient = requests.post("localhost:7700/api/patients/register",
                                    data={"name":row["name"],
                                          "age":row["age"],
                                          "address":row["address"],
                                          "email":row["email"],
                                          "gender":row["gender"]})
    
    print(new_patient)
    
@then("increases Patient Count from API")
def check_count_increase(context):
    ok_(context.currentCount<len(requests.get(
        "ocalhost:7700/api/patients/list").json()),"Patient Registration Failed")