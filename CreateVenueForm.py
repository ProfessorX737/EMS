from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, DateTimeField, IntegerField, SubmitField, SelectField

class CreateVenueForm(Form):
    name = StringField('Name', validators=[validators.DataRequired("Please enter venue location.")])
    location = StringField('Location', validators=[validators.DataRequired("Please enter venue location.")])
    capacity = IntegerField('Capacity', validators=[validators.DataRequired("Please enter the location capacity.")])
    submit = SubmitField('Add Venue', validators=(validators.Optional(),))

