'''
Created on 13 Feb 2019

@author: Eleanor61082
'''
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from mysql import connector
import jsonpickle

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/graduate_training'
db = SQLAlchemy(app)

class Patient_data(object):
     
     def __init__(self,params):
        self.patient_id = int(params["patient_id"])
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
        self.name=params["name"]
        self.age=int(params["age"])
        self.address=params["address"]
        pass
    
    def display_information(self):
        print("Patient Id:",self.patient_id,"Name:",self.name,"Age:",self.age,
              "Address:",self.address)
        
    @staticmethod
    def fetch_all_patients_from_db():
        cnx = connector.connect(user='root',password='root',
                                database='graduate_training',port=3306)
        cur = cnx.cursor()
        cur.execute('select * from alc_Patients')
        patients = []
        for(patient_id,name,age,address) in cur:
            patients.append(Patient_data({"patient_id":patient_id,"name":name,
                                     "age":age,"address":address}))
        cur.close()
        cnx.close()
        return jsonpickle.encode(patients)
    def __str__(self):
        return "Patient Id:"+str(self.patient_id)+"Name:"+self.name+"Age:"+str(self.age)+"Address:"+self.address


    
    @staticmethod
    def fetch_patient_by_patient_id_from_db(patient_id):
        cnx = connector.connect(user='root',password='root',
                                database='graduate_training',port=3306)
        cur = cnx.cursor()
        cur.execute('select * from alc_Patients where patient_id = '+str(patient_id))
        patient=None
        for(patient_id,name,age,address) in cur:  #fetch each column data from the cursor
            patient = Patient_data({"patient_id":patient_id,"name":name,
                                     "age":age,"address":address})
        cur.close()
        cnx.close()
        return patient
    
    @staticmethod
    def insert_patient_in_db(new_patient):
        #1st Connect to DB
        cnx = connector.connect(user='root',password='root',
                                database='graduate_training',port=3306)
        
        #2nd fetching the cursor
        cur = cnx.cursor()
        
        #3rd sql query to identify execution, wanting to pass employee data
            #use the cursor and executing the template query
        cur.execute('insert into emp_data_python values(%s,%s,%s)', #%S = parameters to be passed
                    (new_patient.patient_id,new_patient.name,new_patient.age,
                     new_patient.address))
        
        #4th commit all the queries if DML
        cnx.commit()
         
        #5th close the resources
        cur.close()
        cnx.close()

@app.route('/patients')
def example_Patient():
    p = Patient({"name":"Example 2","age":46,"address":"New Address 2"})
    db.session.add(p)
    db.session.commit()
    patients = Patient.query.all()
    for p in patients:
        print("Id: ",p.patient_id,"Name: ",p.name,"Age: ",p.age,"Address: ",p.address)
        
    return str(patients)    
    
    



if __name__ == '__main__':
    # db.create_all()
    # example_Patient()
    print("List of Patients in alc_Patients table")
    for p in Patient.fetch_all_patients_from_db():
        print(p) 
    print(Patient.fetch_patient_by_patient_id_from_db(2))
    pass