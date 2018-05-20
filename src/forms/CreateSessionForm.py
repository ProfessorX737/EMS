from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, DateTimeField, SubmitField, SelectField, IntegerField
from src.validators.dateTime_isLessThan import *
from src.validators.dateTime_isGreaterThan import *

class CreateSessionForm(Form):
    name = StringField('Name', validators=[validators.DataRequired("Please enter event name.")])
    description = StringField('Description', validators=[validators.DataRequired("Please enter event description.")])
    startDateTime = DateTimeField('Start Date Time', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired("Please enter the event start date and time."),LessThan('endDateTime','start < end')])
    endDateTime = DateTimeField('End Date Time', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired("Please enter the event end date and time."), GreaterThan('startDateTime','end > start')])
    capacity = IntegerField('Capacity', validators=[validators.DataRequired("Please enter valid event capacity.")])
    #convener = StringField('Convener Name', validators=[validators.DataRequired("Please enter event convener's name.")])
    presenter = SelectField('Presenter')
    submit = SubmitField('Create Session', validators=(validators.Optional(),))

    def createPairs(self, presenters):
        pairs = []
        for presenter in presenters:
            pairs.append((presenter.get_id(),presenter.getName()))
        return pairs

    def __init__(self,presenters,*args,**kwargs):
        super(CreateSessionForm, self).__init__(*args, **kwargs)
        self.presenter.choices = self.createPairs(presenters)

    def fillDefault(self,event):
        self.name.default = event.getName()
        self.description.default = event.getDescription()
        self.startDateTime.default = event.getStartDateTime().strftime("%Y-%m-%d %H:%M")
        self.endDateTime.default = event.getEndDateTime().strftime("%Y-%m-%d %H:%M") 
        #self.convener.default = event.getConvener()  
        self.presenter.default = (event.getPresenterId(), event.getPresenterName())  
        self.capacity.default = event.getCapacity()