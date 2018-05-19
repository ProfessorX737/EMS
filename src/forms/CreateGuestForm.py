from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, DateTimeField, IntegerField, SubmitField, SelectField, PasswordField
from wtforms.fields.html5 import EmailField

class CreateGuestForm(Form):
    name = StringField('Name', validators=[validators.DataRequired("Please enter fullname.")])
    username = StringField('Username', validators=[validators.DataRequired("Please enter username.")])
    email = EmailField('Email', validators=[validators.DataRequired("Please enter email.")])
    password = PasswordField('Password', validators=[validators.DataRequired("Please enter password.")])
    submit = SubmitField('Register', validators=(validators.Optional(),))
