from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField



class AddPuppyForm(FlaskForm):

    name = StringField('Name of Puppy:')
    age = IntegerField('Age of Puppy: ')
    spots = IntegerField('How many spots does this puppy have: ')
    robot = BooleanField('Check the box if this puppy is a robot:')
    submit = SubmitField('Add Puppy')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner:')
    puppy_id = IntegerField('Id of Puppy: ')
    submit = SubmitField('Add Owner')

class DelForm(FlaskForm):

    id = IntegerField('ID# of the Puppy:')
    submit = SubmitField('Remove Puppy')