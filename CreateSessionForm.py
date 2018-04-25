from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, DateTimeField, SubmitField, SelectField

class CreateSessionForm(Form):
    name = StringField('Name', validators=[validators.DataRequired("Please enter event name.")])
    description = StringField('Description', validators=[validators.DataRequired("Please enter event description.")])
    startDateTime = DateTimeField('Start Date Time', format='%d-%m-%Y %H:%M', validators=[validators.DataRequired("Please enter the event start date and time.")])
    endDateTime = DateTimeField('End Date Time', format='%d-%m-%Y %H:%M', validators=[validators.DataRequired("Please enter the event end date and time.")])
    convener = StringField('Convener Name', validators=[validators.DataRequired("Please enter event convener's name.")])
    submit = SubmitField('Create Event', validators=(validators.Optional(),))

