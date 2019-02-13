'''
Created on 13 Feb 2019

@author: Eleanor61082
'''
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
import jsonpickle
from flask.globals import request

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/graduate_training'
db = SQLAlchemy(app)

@app.route('/')
def application_home():
    return 'Welcome to Medical Records Application'

class Patient_data(object):
     
    def __init__(self,params):
        self.name=params["name"]
        self.age=int(params["age"])
        self.address=params["address"]

class Patient(db.Model):
    
    __tablename__="alc_Patients"
    patient_id = db.Column(db.Integer,primary_key=True)
    name = db.Column('patient_name',db.String(50))
    age = db.Column(db.Integer)
    address = db.Column('patient_address',db.String(50))
    
    def __init__(self,params):
        #self.patient_id = int(params["patient_id"])
        self.name=params["name"]
        self.age=int(params["age"])
        self.address=params["address"]
        pass
            
    #def __str__(self):
    #   return "Patient Id:"+str(self.patient_id)+"Name:"+self.name+"Age:"+str(self.age)+"Address:"+self.address
    

@app.route('/patients')
def example_Patient():
    p = Patient({"name":"Example 2","age":46,"address":"New Address 2"})
    db.session.add(p)
    db.session.commit()
    patients = Patient.query.all()
    for p in patients:
        print("Id: ",p.patient_id,"Name: ",p.name,"Age: ",p.age,"Address: ",p.address)
        
    return str(patients)    

@app.route('/api/patients/register',methods=['POST'])
def insert_Patient():
    p=db.session.add(Patient({"name":"Example 4","age":48,"address":"New Address 4"}))

    db.session.commit()
    patients = Patient.query.all()
    for p in patients:
        print("Id: ",p.patient_id,"Name: ",p.name,"Age: ",p.age,"Address: ",p.address)
        
    return str(patients) 
    
@app.route('/api/patients/list')
def fetch_patients():
    return jsonpickle.encode(Patient.query.all())


    



if __name__ == '__main__':
    # db.create_all()
    # example_Patient()
#     print("List of Patients in alc_Patients table")
#     for p in Patient.fetch_all_patients_from_db():
#         print(p) 
#     print(Patient.fetch_patient_by_patient_id_from_db(2))
    app.run(port=7700)
    pass