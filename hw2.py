import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddPuppyForm , AddOwnerForm , DelForm

##



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sha2user:Boot!camp2021!@localhost/adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

##


class Puppy(db.Model):

    __tablename__ = 'ListofPuppies'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    spots = db.Column(db.Integer)
    robot = db.Column(db.Boolean)
    owner = db.relationship('Owner', backref='puppy', uselist=False)
    
    
    def __init__(self, name, age, spots, robot):
    
        self.name = name
        self.age = age
        self.spots = spots
        self.robot = robot
    
    def __repr__(self):
        if self.owner:
            return f"{self.name} is owned by {self.owner.name}"
        else:
            return f"{self.name} does not have an owner yet."
 
 
class Owner(db.Model):

    __tablename__ = 'ListofOwners'
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('ListofPuppies.id'))
    
    def __init__(self, name, puppy_id):
    
        self.name = name
        self.puppy_id = puppy_id
    
    def __repr__(self):
        if self.puppy_id:
            return f"{self.name} is the owner of puppy with ID {self.puppy_id}"
        else:
            return f"Owner name: {self.name}"
 
##

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/AddPuppy', methods=['GET', 'POST'])
def addpuppy():

    form = AddPuppyForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        spots = form.spots.data
        robot = form.robot.data
        new_pup = Puppy(name, age, spots, robot)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('thankyou'))
    return render_template('addpuppy.html', form=form)


@app.route('/AddOwner', methods=['GET', 'POST'])
def addowner():
    form = AddOwnerForm()
    
    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data
        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('thankyou'))
    return render_template('addowner.html', form=form)
    
@app.route('/listPuppy')
def listpuppy():
  
    ListofPuppies = Puppy.query.all()
    return render_template('listp.html', ListofPuppies=ListofPuppies)
    
@app.route('/listOwner') 
def listowner():
    ListofOwners = Owner.query.all()
    
    return render_template('listo.html', ListofOwners=ListofOwners)


@app.route('/delete',  methods=['GET', 'POST'])
def delpuppy():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('thankyou'))
    return render_template('delete.html',form=form)
    
@app.route('/thankyou') 
def thankyou():
    return render_template('thankyou.html')


def read():
   
    df = pd.read_csv('t.csv')
    return render_template('listp.html', df=df)
    

def page_not_found(e):
    return render_template('error.html')
    
if __name__ == '__main__':
    app.run(debug=True)