'''
Created on 13 Feb 2019

@author: Eleanor61082
'''
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
import jsonpickle
from flask.globals import request
from sqlalchemy.orm import backref
from werkzeug.utils import redirect

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/medical_data'
db = SQLAlchemy(app)


@app.route('/')
def application_home():
    return 'Welcome to Medical Records Application'

class Patient(db.Model):
    
    __tablename__="alc_Patients"
    
    patient_id = db.Column(db.Integer,primary_key=True)
    name = db.Column('patient_name',db.String(50))
    age = db.Column(db.Integer)
    address = db.Column('patient_address',db.String(50))
    email = db.Column('patient_email',db.String(50))
    gender = db.Column('gender',db.String(10))
    
    #one patient has many reports
    reports = db.relationship('Report',backref=db.backref('patient'),lazy=True)
    
    #many patients for one lab manager
    lab_manager_id = db.Column(db.Integer,
                           db.ForeignKey('alc_Lab_Manager.lab_manager_id'),
                           nullable=False)

    def __init__(self,params):
        #self.patient_id = int(params["patient_id"])
        self.name=params["name"]
        self.age=int(params["age"])
        self.address=params["address"]
        self.email=params["email"]
        self.gender=params["gender"]

        pass
    
class Report(db.Model):
    
    __tablename__="alc_Reports"
    report_id = db.Column(db.Integer,primary_key=True)
    title = db.Column('report_title',db.String(50))
    related_illness=db.Column('related_illness',db.String(50))
    date=db.Column('date',db.String(50))
    notes = db.Column('notes',db.String(300))
    perscription = db.Column('prescription',db.String(20))
    
    #many reports for one patient
    patient_id = db.Column(db.Integer,
                           db.ForeignKey('alc_Patients.patient_id'),
                           nullable=False)
    
    #many reports for one lab manager
    #lab_manager_id = db.Column(db.Integer,
    #                       db.ForeignKey('alc_Lab_Manager.lab_manager_id'),
    #                       nullable=False)
    
    def __init__(self,params):
        self.title=params["title"]
        self.related_illness=params["related_illness"]
        self.date=params["date"]
        self.notes=params["notes"]
        self.perscription=params["perscription"]


class Lab_Manager(db.Model):
    
    __tablename__="alc_Lab_Manager"
    lab_manager_id = db.Column(db.Integer,primary_key=True)
    name = db.Column('lab_manager_name',db.String(50))
    location = db.Column('lab_manager_location',db.String(50))
    test = db.Column('lab_manager_test',db.String(50))
    result = db.Column('lab_manager_result',db.String(50))

    #one lab manager has many reports
    #reports = db.relationship('Report',
    #                                     backref=db.backref('labManager'),lazy=True)
    #one lab manager has many patients
    patients = db.relationship('Patient',
                                         backref=db.backref('labManager'),lazy=True)
    
    def __init__(self,params):
        self.name=params["name"]
        self.test=params["test"]
        self.result=params["result"]
        pass   
            
@app.route('/patients')
def example_Patient():
    p = Patient({"name":"Example 3","age":55,"address":"New Address 3","email":"example@hotmail.com",
                 "gender":"Male"})
    l = Lab_Manager({"name":"Dr Jones","test":"MRA","result":"Clear"})
    
    l.patients.append(p)
    db.session.add(p)
    db.session.add(l)
    
    db.session.commit()
    patients = Patient.query.all()
    for p in patients:
        print("Id: ",p.patient_id,"Name: ",p.name,"Age: ",p.age,"Address: ",p.address,
              "Email: ",p.email,"Gender: ",p.gender)
        
    return str(patients)

@app.route('/reports')
def example_Report():
    r = Report({"title":"Report 3","related_illness":"illness 3","date":"11.11.2018",
                "notes":"note example 3","perscription":"example 3"})
    
    p = Patient({"name":"Patient with Report","age":25,"address":"Patient Address",
                 "email":"example@gmail.com","gender":"Male"})
    
    #l = Lab_Manager({"name":"Dr Steve","test":"Blood Test","result":"Clear"})
    
    p.reports.append(r)
    #l.reports.append(r)
    
    db.session.add(r)
    db.session.add(p)
    #db.session.add(l)
    
    db.session.commit()
    reports = Report.query.all()
    for r in reports:
        print("Id: ",r.report_id,"Title: ",r.title,"Related Illness: ",r.related_illness,
              "Date: ",r.date,"Notes: ",r.notes,"Prescription: ",r.perscription)
        
    return str(reports)

@app.route('/api/labmanager')
def example_Lab_Manager():
    lm = Lab_Manager({"name":"Dr Farquad","test":"XRay","result":"Broken Forearm"})
    db.session.add(lm)
    db.session.commit()
    labManager = Lab_Manager.query.all()
    for lm in labManager:
        print("Id: ",lm.lab_manager_id,"Name: ",lm.name,"Test: ",
              lm.test,"Result: ",lm.result)
        
    return str(labManager)      

@app.route('/api/patients/register',methods=['POST'])
def insert_Patient():
    #p=db.session.add(Patient({"name":"Example 4","age":48,"address":"New Address 4"}))
    p = db.session.add(Patient({"name":request.form.get("name"),
                                "age":int(request.form.get("age")),
                                "address":request.form.get("address"),
                                "email":request.form.get("email"),
                                "gender":request.form.get("gender")}))
    db.session.commit()
    patients = Patient.query.all()
    for p in patients:
        print("Id: ",p.patient_id,"Name: ",p.name,"Age: ",p.age,"Address: ",p.address,
              "Email: ",p.email,"Gender :",p.gender)
        
    return str(patients)

@app.route('/web/patients/register',methods=['POST'])
def register_patient_web():
    insert_Patient(Patient({"name":request.form.get("name"),
                                "age":int(request.form.get("age")),
                                "address":request.form.get("address"),
                                "email":request.form.get("email"),
                                "gender":request.form.get("gender")}))
    return redirect("/web/patients")

@app.route('/api/reports/register',methods=['POST'])
def insert_Report():
    r = Report({"title":request.form.get("title"),
                               "related_illness":request.form.get("related_illness"),
                               "date":request.form.get("date"),
                               "notes":request.form.get("notes"),
                               "perscription":request.form.get("perscription")})
    db.session.add(r)
    
    p = Patient.query.filter_by(patient_id=request.form.get('patient_id')).first()
    p.reports.append(r)

    print(p)
    print(p.reports)
    
    db.session.commit()
    reports = Report.query.all()
    for r in reports:
        print("Id: ",r.report_id,"Title: ",r.title,"Related Illness: ",r.related_illness,
              "Date: ",r.date,"Notes: ",r.notes,"Perscription: ",r.perscription,"Patient Id: ",r.patient_id)
    return str(reports) 

@app.route('/web/reports/register',methods=['POST'])
def register_report_web():
    insert_Report(
        Report({"title":request.form.get("title"),
                               "related_illness":request.form.get("related_illness"),
                               "date":request.form.get("date"),
                               "notes":request.form.get("notes"),
                               "perscription":request.form.get("perscription"),
                               "patient_id":request.form.get("patient_id")}))
    db.session.commit()
    return redirect("/web/patients")

@app.route('/api/labmanager/register',methods=['POST'])
def insert_Lab_Manager():   
    lm = db.session.add(Lab_Manager({"name":request.form.get("name"),
                                "test":request.form.get("test"),
                                "result":request.form.get("result")}))
    db.session.commit()
    labManager = Lab_Manager.query.all()
    
    for lm in labManager:
        print("Id: ",lm.lab_manager_id,"Name: ",lm.name,"Test: ",
              lm.test,"Result: ",lm.result)
        
    return str(labManager)    

@app.route('/api/labmanager/delete/<int:lab_manager_id>', methods = ['DELETE'])
def delete_lab_manager(lab_manager_id):
    labmanager = Lab_Manager.query.get(int(lab_manager_id))
    db.session.delete(labmanager)
    db.session.commit()
    return jsonpickle.encode(labmanager)

@app.route("/api/labmanager/update/<int:lab_manager_id>",methods=['POST'])
def edit_lab_manager_reports(lab_manager_id):
    request_data = request.get_json()
    lbmg = Lab_Manager.query.get(int(lab_manager_id))
    lbmg.name = request_data["name"]
    lbmg.location = request_data["location"]
    lbmg.test = request_data["test"]
    lbmg.result = request_data["result"]
    db.session.commit()
    return_lab_manager = {"lab_manager_id":lbmg.lab_manager_id,"name":lbmg.name,
                     "location":lbmg.location,"test":lbmg.test,"result":lbmg.result}
    return jsonpickle.encode(return_lab_manager)

@app.route('/api/reports/list')
def fetch_reports():
    return jsonpickle.encode(Report.query.all())
    
@app.route('/api/patients/list')
def fetch_patients():
    return jsonpickle.encode(Patient.query.all())

@app.route('/api/labmanager/list')
def fetch_Lab_Managers():
    return jsonpickle.encode(Lab_Manager.query.all())


if __name__ == '__main__':

#    db.create_all()
#    example_Patient()
#    example_Lab_Manager()
#    example_Report()
#    example_Lab_Manager()
#     print("List of Patients in alc_Patients table")
#     for p in Patient.fetch_all_patients_from_db():
#         print(p) 
#     print(Patient.fetch_patient_by_patient_id_from_db(2))
    app.run(port=7700)
    pass