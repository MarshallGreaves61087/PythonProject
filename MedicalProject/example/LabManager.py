'''
Created on 13 Feb 2019

@author: Marshal61087
'''
from flask_sqlalchemy import SQLAlchemy
from flask.app import Flask
import jsonpickle
from flask.globals import request

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/medical_data'
db = SQLAlchemy(app)

class Lab_Manager(db.Model):
    
    __tablename__="alc_Lab_Manager"
    lab_manager_id = db.Column(db.Integer,primary_key=True)
    name = db.Column('lab_manager_name',db.String(50))
    location = db.Column('lab_manager_location',db.String(50))
    test = db.Column('lab_manager_test',db.String(50))
    result = db.Column('lab_manager_result',db.String(50))
    
    reports = db.relationship('Report',
                                         backref=db.backref('lab_manager'),lazy=True)
    
    def __init__(self,params):
        self.name=params["name"]
        self.location=params["location"]
        self.test=params["test"]
        self.result=params["result"]
        pass
            
@app.route('/api/labmanager')
def example_Lab_Manager():
    lm = Lab_Manager({"name":"Dr Farquad","location":"Bristol","test":"XRay","result":"Broken Forearm"})
    db.session.add(lm)
    db.session.commit()
    labManager = Lab_Manager.query.all()
    for lm in labManager:
        print("Id: ",lm.lab_manager_id,"Name: ",lm.name,"Location: ",lm.location,"Test: ",
              lm.test,"Result: ",lm.result)
        
    return str(labManager)    

@app.route('/api/labmanager/register',methods=['POST'])
def insert_Lab_Manager():   
    lm = db.session.add(Lab_Manager({"name":request.form.get("name"),
                                     "location":request.form.get("location"),
                                     "test":request.form.get("test"),
                                     "result":request.form.get("result")}))
    db.session.commit()
    labManager = Lab_Manager.query.all()
    for lm in labManager:
        print("Id: ",lm.lab_manager_id,"Name: ",lm.name,"Location: ",lm.location,"Test: ",
              lm.test,"Result: ",lm.result)
        
    return str(labManager)    

@app.route('/api/labmanager/list')
def fetch_Reports():
    return jsonpickle.encode(Lab_Manager.query.all())

@app.route('/api/labmanager/delete/<int:lab_manager_id>', methods = ['DELETE'])
def delete_lab_manager(lab_manager_id):
    labmanager = Lab_Manager.query.get(int(lab_manager_id))
    db.session.delete(labmanager)
    db.session.commit()
    return jsonpickle.encode(labmanager)

if __name__ == '__main__':
    #db.create_all()    #creates database
    #example_Lab_Manager()
    
    app.run(port=7700)
    pass