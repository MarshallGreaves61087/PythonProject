import behave
from nose.tools.trivial import ok_
from example import MedicalApplication, LabManager
#from pip._vendor import requests



@given("Request for All Lab_Managers")
#def fetch_lab_manager_from_api(context):
#    context.labManagers = requests.get("http://localhost:7700/api/labmanager/list").json()
    
@then("have all lab_managers available from application")
def check_all_lab_managers_present(context):
    ok_(len(context.labs)>0,"Lab Managers Not Available")
'''    
@given("a set lb for API")
def post_lab_manager_data_to_API(context):
    context.currectCount = len(requests.get("http://localhost:7700/api/labmanager/list").json())
    for row in context.table:
        new_lab = requests.post("http://localhost:7700/api/labmanager/register",
                                    data={"lab_manager_id":row["lab_manager_id"],
                                      "name":row["name"],"test":row["test"],
                                      "result":row["result"]})
        print(new_lab)
    for row in context.table:
        context.labs.append(row["lab_manager_id"])
        if(not isinstance(MedicalApplication.fetch_Lab_Managers(row["lab_manager_id"]),LabManager)):
            MedicalApplication.insert_Lab_Manager({"lab_manager_id":row["lab_manager_id"],
                                      "name":row["name"],"test":row["test"],
                                      "result":row["result"]})'''
    
@then("increase the Lab_Manager Count from API")
def check_count_increase(context):
    ok_(not(context.count_text == context.driver.find_element_by_id("count").text),
        "count not changed")