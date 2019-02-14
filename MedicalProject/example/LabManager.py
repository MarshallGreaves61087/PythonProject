'''
Created on 13 Feb 2019

@author: Marshal61087
'''
from flask_sqlalchemy import SQLAlchemy
from flask.app import Flask
import jsonpickle
from flask.globals import request

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/graduate_training'
db = SQLAlchemy(app)

class Lab_Manager_data(object):
     
    def __init__(self,params):
        self.name=params["name"]
        self.test=int(params["test"])
        self.result=params["result"]

class Lab_Manager(db.Model):
    
    __tablename__="Lab_Manager"
    lab_manager_id = db.Column(db.Integer,primary_key=True)
    name = db.Column('lab_manager_name',db.String(50))
    test = db.Column('lab_manager_test',db.String(50))
    result = db.Column('lab_manager_result',db.String(50))
    
    def __init__(self,params):
        self.name=params["name"]
        self.test=params["test"]
        self.result=params["result"]
        pass
            
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

@app.route('/api/labmanager/list')
def fetch_Reports():
    return jsonpickle.encode(Lab_Manager.query.all())

if __name__ == '__main__':
    #db.create_all()    #creates database
    #example_Lab_Manager()
    
    app.run(port=7700)
    pass