'''
Created on 13 Feb 2019

@author: Eleanor61082
'''
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/graduate_training'
db = SQLAlchemy(app)

class Report(db.Model):
    
    __tablename__="alc_Reports"
    report_id = db.Column(db.Integer,primary_key=True)
    title = db.Column('report_title',db.String(50))
    related_illness=db.Column('related_illness',db.String(50))
    date=db.Column('date',db.String(50))
    notes = db.Column('notes',db.String(300))
    perscription = db.Column('perscription',db.String(20))