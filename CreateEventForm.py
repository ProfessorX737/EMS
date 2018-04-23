from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, DateTimeField, SubmitField, SelectField

class CreateEventForm(Form):
    eventChoices = [('Course','Course'),('Seminar','Seminar')]
    eventType = SelectField('Event Type', choices=eventChoices, validators=[validators.DataRequired("Please pick event type")])
    name = StringField('Event Name', validators=[validators.DataRequired("Please enter event name.")])
    description = StringField('Description', validators=[validators.DataRequired("Please enter event description.")])
    startDateTime = DateTimeField('Start Date Time', format='%d-%m-%Y %H:%M', validators=[validators.DataRequired("Please enter the event start date and time.")])
    endDateTime = DateTimeField('End Date Time', format='%d-%m-%Y %H:%M', validators=[validators.DataRequired("Please enter the event end date and time.")])
    deregEnd = DateTimeField('Deregister Period End', format='%d-%m-%Y %H:%M', validators=[validators.DataRequired("Please enter the end of deregistration period.")])
    convener = StringField('Convener Name', validators=[validators.DataRequired("Please enter event convener's name.")])
    venue = StringField('Venue', validators=[validators.DataRequired("Please enter the event venue.")])
    capacity = StringField('Capacity', validators=[validators.DataRequired("Please enter the event capacity.")])
    submit = SubmitField('Create Event', validators=(validators.Optional(),))

