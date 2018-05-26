from flask_wtf import Form
from wtforms import SubmitField, SelectField

class SelectEventForm(Form):
    makeCourse = SubmitField('Make a Course')
    makeSeminar = SubmitField('Make a Seminar')