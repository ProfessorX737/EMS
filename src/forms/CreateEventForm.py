from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, DateTimeField, IntegerField, SubmitField, SelectField
from src.validators.dateTime_isLessThan import *
from src.validators.dateTime_isGreaterThan import *
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
    startDateTime = DateTimeField('Start Date Time', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired("Please enter the event start date and time."),LessThan('endDateTime','start < end')])
    endDateTime = DateTimeField('End Date Time', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired("Please enter the event end date and time."), GreaterThan('startDateTime','end > start')])
    deregEnd = DateTimeField('Deregister Period End', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired("Please enter the end of deregistration period."), LessThan('startDateTime', 'dereg < start')])
    earlybirdEnd = DateTimeField('Earlybird Period End', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired("Please enter the end of earlybird period."), LessThan('startDateTime', 'earlybird< start')])
    fee = IntegerField('Registration Fee', validators=[validators.DataRequired("Please enter valid registration fee.")])
    convener = StringField('Convener Name', validators=[validators.DataRequired("Please enter event convener's name.")])
    venue = SelectField('Venue')
    capacity = IntegerField('Capacity', validators=[validators.DataRequired("Please enter valid event capacity.")])
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

    def fillDefault(self,event):
        self.name.default = event.getName()
        self.description.default = event.getDescription()
        self.startDateTime.default = event.getStartDateTime().strftime("%Y-%m-%d %H:%M")
        self.endDateTime.default = event.getEndDateTime().strftime("%Y-%m-%d %H:%M") 
        self.venue.default = (event.getVenueName(), event.getVenueName())
        self.convener.default = event.getConvener()  
        self.capacity.default = event.getCapacity()
        self.deregEnd.default = event.getDeregEnd().strftime("%Y-%m-%d %H:%M")
        self.fee.default = event.getFee()
        self.earlybirdEnd.default = event.getEarlyBirdEnd().strftime("%Y-%m-%d %H:%M")