from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, DateTimeField, IntegerField, SubmitField, SelectField

# Enables us to pass parameters into WTForm 
class NewStartUpForm( Form ):
    def __init__( self, venues, *arg, **kwarg ):
        self.venues = venues
    def getForm( self, *arg, **kwarg ):
        venues=self.venues
        return CreateEventForm(venues)

class CreateEventForm(Form):
    eventChoices = [('Course','Course'),('Seminar','Seminar')]
    eventType = SelectField('Event Type', choices=eventChoices,validators=(validators.Optional(),))
    name = StringField('Name', validators=[validators.DataRequired("Please enter event name.")])
    description = StringField('Description', validators=[validators.DataRequired("Please enter event description.")])
    startDateTime = DateTimeField('Start Date Time', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired("Please enter the event start date and time.")])
    endDateTime = DateTimeField('End Date Time', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired("Please enter the event end date and time.")])
    deregEnd = DateTimeField('Deregister Period End', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired("Please enter the end of deregistration period.")])
    convener = StringField('Convener Name', validators=[validators.DataRequired("Please enter event convener's name.")])
    venue = SelectField('Venue')
    capacity = IntegerField('Capacity', validators=[validators.DataRequired("Please enter the event capacity.")])
    submit = SubmitField('Create Event', validators=(validators.Optional(),))

    # SelectFields must be provided with pair objects
    def createPairs(self, venues):
        pairs = []
        for venue in venues:
            pairs.append((venue,venue))
        return pairs

    def __init__(self,venues, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.venue.choices = self.createPairs(venues)

   
