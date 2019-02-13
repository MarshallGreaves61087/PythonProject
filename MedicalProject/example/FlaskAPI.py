'''
Created on 13 Feb 2019

@author: Eleanor61082
'''
from flask import Flask
import jsonpickle
from example.MedicalApplication import Patient, Patient_data
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def application_home():
    return 'Welcome to Medical Records Application'




@app.route('/api/patients/register',methods=['POST'])
def register_patient():
    Patient.insert_patient_in_db(
        Patient_data({
                 "name":request.form.get("name"),
                 "age":int(request.form.get("age")),
                 "address":request.form.get("address")}))
    return jsonpickle.encode(Patient.fetch_all_patients_from_db())

if __name__ == '__main__':
    app.run(port=7700)