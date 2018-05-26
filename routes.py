import copy
import os
from flask import Flask, render_template, url_for, flash, request, redirect, session
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from src.UserManager import *
from src.EventManager import *
from src.Event import *
from src.Period import *
from src.Seminar import *
from src.Course import *
from src.forms.CreateEventForm import *
from src.forms.CreateSessionForm import *
from src.forms.CreateVenueForm import *
from src.forms.CreateGuestForm import *
from src.forms.SelectEventForm import *
from src.exceptions.LoginException import *
from src.exceptions.VenueCapacityException import *
from src.exceptions.ExistingEventException import *
from src.exceptions.ExistingVenueException import *
from Server import app, ems, loadUser
from urllib.parse import quote_plus, unquote_plus
app.jinja_env.filters['quote_plus'] = quote_plus

try:
    with open('user.csv') as f:
        lines = f.readlines()
        for line in lines:
            attr = line.split(',')
            # remove new line character from last elt
            attr[-1] = attr[-1].strip()
            ems.addUser(attr[0],attr[1],attr[2],attr[3],attr[4])
except OSError as e:
    print(e)
    exit()

@app.route('/',methods=['GET','POST'])
def login():
    if (request.method == 'POST'):
        zid = request.form.get('zid','')
        password = request.form.get('password','')
        try:
            user = ems.getUserById(zid)
            ems.checkPassword(user,password)
            login_user(user)
            # Store user type globally after user logs in so we can keep track if they are Staff or Student
            global userType
            userType = ems.getUserType(current_user.get_id())
            return redirect(url_for('home'))
        except LoginException as errmsg:
            return render_template('login.html',message= errmsg.args[1])
    return render_template('login.html')

@app.route('/home',methods=['GET','POST'])
@login_required
def home():
    return render_template('home.html',userType = userType,seminars = ems.getCurrentSeminars(), courses = ems.getCurrentCourses())

@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html',userType=userType)

@app.route('/register_guest',methods=['GET','POST'])
def register_guest():
    form = CreateGuestForm()
    if form.validate_on_submit():
        if ems.userIdExists(form.username.data):
            return render_template('register.html', form = form, message = 'That username already exists')
        elif ems.userEmailExists(form.email.data):
            return render_template('register.html', form = form, message = 'That email already exists')
        else:
            guest = ems.addUser(form.name.data, form.username.data, form.email.data, form.password.data, 'guest')
            return render_template('login.html',message="You have successfully registered.")
    return render_template('register.html', form = form)

@app.route('/create_event',methods=['GET','POST'])
@login_required
def create_event():
    form = SelectEventForm()
    if form.validate_on_submit():
        if form.makeCourse.data == True:
            return redirect(url_for('create_course'))
        elif form.makeSeminar.data == True:
            return redirect(url_for('create_seminar'))
    return render_template('select_event.html',form=form)

@app.route('/create_course',methods=['GET','POST'])
@login_required
def create_course():
    venues = ems.getVenues()
    form = CreateEventForm(venues)
    message = ''
    if form.validate_on_submit():
        try:
            ems.addCourse(current_user,form.startDateTime.data,form.endDateTime.data,
            form.name.data,form.description.data,form.venue.data,copy.copy(current_user),
            form.capacity.data,form.deregEnd.data,form.fee.data,form.earlybirdEnd.data)
            return redirect(url_for('home'))
        except VenueCapacityException as errmsg:
            return render_template('create_event.html', form = form, userType=userType, message=errmsg.args[1], action="/create_course")
        except ExistingEventException as errmsg:
            return render_template('create_event.html', form = form, userType=userType, message=errmsg.args[1], action="/create_course")
    return render_template('create_event.html', form = form, userType=userType, message=message, action="/create_course")

@app.route('/create_seminar',methods=['GET','POST'])
@login_required
def create_seminar():
    venues = ems.getVenues()
    form = CreateEventForm(venues)
    del form.capacity
    message = ''
    if form.validate_on_submit():
        try:
            ems.addSeminar(current_user,form.startDateTime.data,form.endDateTime.data,
            form.name.data,form.description.data,form.venue.data,copy.copy(current_user),
            0,form.deregEnd.data,form.fee.data,form.earlybirdEnd.data)
            return redirect(url_for('home'))
        except VenueCapacityException as errmsg:
            return render_template('create_event.html', form = form, userType=userType, message=errmsg.args[1], action="/create_seminar")
        except ExistingEventException as errmsg:
            return render_template('create_event.html', form = form, userType=userType, message=errmsg.args[1], action="/create_seminar")
    return render_template('create_event.html', form = form, userType=userType, message=message, action="/create_seminar")

@app.route("/more/<eventType>/<eventId>",methods=['GET','POST'])
@login_required
def moreInfo(eventType,eventId):
    eventId = int(eventId)
    event = ems.getEvent(eventId)
    isOwner = ems.isMyEvent(current_user.get_id(),eventId)
    isPresenter = ems.isPresenterAtEvent(current_user.get_id(),eventId)
    if isinstance(event,Session):
        isPresenter = ems.isPresenterAtEvent(current_user.get_id(),event.getSeminarId())
    fee = ems.getCost(eventId,current_user.get_id())
    # if staff check if this event is inside getPostedCurrEvents
    return render_template('more_info.html',isOwner=isOwner,isPresenter=isPresenter,event=event,userType=userType,fee=fee)

@app.route('/create_session/<seminarId>',methods=['GET','POST'])
@login_required
def create_session(seminarId):
    seminarId = int(seminarId)
    presenters = []
    presenters.extend(ems.getGuests())
    presenters.extend(ems.getStaff())
    form = CreateSessionForm(presenters)
    message = ''
    try:
        if form.validate_on_submit():
            presenter = ems.getUserById(form.presenter.data)
            ems.addSession(current_user,seminarId,form.startDateTime.data,form.endDateTime.data,
            form.name.data,form.description.data,form.capacity.data,presenter)
            return redirect(url_for('moreInfo',eventType='Seminar',eventId=seminarId))
    except VenueCapacityException as errmsg:
            return render_template('create_session.html',seminarId=seminarId,form=form,userType=userType, message=errmsg.args[1])
    except ExistingEventException as errmsg:
            return render_template('create_session.html',seminarId=seminarId,form=form,userType=userType, message=errmsg.args[1])
    return render_template('create_session.html',seminarId=seminarId,form=form,userType=userType,message=message)

@app.route('/register/<eventId>',methods=['GET','POST'])
@login_required
def register_user(eventId):
    eventId = int(eventId)
    event = ems.getEvent(eventId)
    if isinstance(event,Course):
        ems.registerUserToCourse(eventId,copy.copy(current_user))
        ems.addRegisteredEvent(current_user.get_id(),event)
    if isinstance(event,Seminar):
        if not event.isRegisteredToASession(current_user.get_id()):
            isOwner = ems.isMyEvent(current_user.get_id(),eventId)
            return render_template('more_info.html',isOwner=isOwner,event=event,userType=userType,regErrorMsg="To register you must be registered to at least one session")
        ems.registerUserToSeminar(eventId,copy.copy(current_user))
        ems.addRegisteredEvent(current_user.get_id(),event)
    if isinstance(event,Session):
        ems.registerUserToSession(eventId,copy.copy(current_user))
        ems.registerUserToSeminar(event.getSeminarId(), copy.copy(current_user))
        seminar = ems.getEvent(event.getSeminarId())
        ems.addRegisteredEvent(current_user.get_id(),seminar) 
        ems.addRegisteredEvent(current_user.get_id(),event)
        return redirect(url_for('moreInfo',eventType=event.getClassName(),eventId=event.getSeminarId()))

    return redirect(url_for('moreInfo',eventType=event.getClassName(),eventId=eventId))

@app.route('/deregister/<eventId>',methods=['GET','POST'])
@login_required
def deregister_user(eventId):
    eventId = int(eventId)
    event = ems.getEvent(eventId)
    ems.removeRegisteredEvent(current_user.get_id(),eventId)
    if isinstance(event,Course):
        ems.deregisterUserFromCourse(eventId,current_user.get_id())
    if isinstance(event,Seminar):
        ems.deregisterUserFromSeminar(eventId,current_user.get_id())
        for session in event.getSessions():
            ems.deregisterUserFromSession(session.getId(),current_user.get_id())      
            ems.removeRegisteredEvent(current_user.get_id(),session.getId())
    if isinstance(event,Session):
        ems.deregisterUserFromSession(eventId,current_user.get_id())
        seminar = ems.getEvent(event.getSeminarId())
        if not seminar.isRegisteredToASession(current_user.get_id()):
            ems.deregisterUserFromSeminar(event.getSeminarId(),current_user.get_id())
            ems.removeRegisteredEvent(current_user.get_id(),event.getSeminarId())
        return redirect(url_for('moreInfo',eventType=event.getClassName(),eventId=event.getSeminarId()))
    return redirect(url_for('moreInfo',eventType=event.getClassName(),eventId=eventId))

@app.route('/edit_event/<eventType>/<eventId>',methods=['GET','POST'])
@login_required        
def edit_event(eventType,eventId):
    eventId = int(eventId)
    event = ems.getEvent(eventId)
    venues = ems.getVenues()
    #form = NewStartUpForm(venueNames).getForm()
    form = CreateEventForm(venues)
    form.fillDefault(event)
    form.eventType.data = event.getClassName()
    message=''
    if form.validate_on_submit():
        try:
            ems.setEvent(event,form.startDateTime.data,form.endDateTime.data,form.name.data,\
            form.description.data,form.venue.data,form.capacity.data,form.deregEnd.data,form.fee.data,form.earlybirdEnd.data)
            return redirect(url_for('home'))
        except VenueCapacityException as errmsg:
            return render_template('edit_event.html',form=form,event=event,message=errmsg.args[1])
    return render_template('edit_event.html',form=form,event=event,message=message)

@app.route('/edit_session/<eventType>/<eventId>',methods=['GET','POST'])
@login_required        
def edit_session(eventType,eventId):
    eventId = int(eventId)
    event = ems.getEvent(eventId)
    presenters = []
    presenters.extend(ems.getGuests())
    presenters.extend(ems.getStaff())
    form = CreateSessionForm(presenters)
    form.fillDefault(event)
    message=''
    if form.validate_on_submit():
        if (event.getNumAttendees() > form.capacity.data):
            message='new capacity must be >= current number of attendees'
            return render_template('edit_session.html',form=form,event=event,message=message)
        presenter = ems.getUserById(form.presenter.data)
        ems.editSession(event,form.startDateTime.data,form.endDateTime.data,form.name.data,\
        form.description.data,presenter,form.capacity.data)
        return redirect(url_for('home'))
    return render_template('edit_session.html',form=form,event=event,message=message)

@app.route('/cancel_event/<eventType>/<eventId>',methods=['GET','POST'])
@login_required        
def cancel_event(eventType,eventId):
    eventId = int(eventId)
    ems.cancelEvent(eventId)
    return redirect(url_for('home'))

@app.route('/delete_venue/<venueId>',methods=['GET','POST'])
@login_required
def delete_venue(venueId):
    venueId = int(venueId)
    ems.removeVenue(venueId)
    return redirect(url_for('view_venues'))

@app.route('/create_venue',methods=['GET','POST'])
@login_required
def create_venue():
    form = CreateVenueForm()
    message = ''
    if form.validate_on_submit():
        try:
            ems.addVenue(form.name.data,form.location.data,form.capacity.data) 
            return redirect(url_for('view_venues'))
        except ExistingVenueException as errmsg:
            message = errmsg.args[1]
    return render_template('create_venue.html',form=form,userType=userType,message=message)

@app.route('/venues',methods=['GET','POST'])
@login_required
def view_venues():
    venues = ems.getVenues()
    return render_template('venues.html',venues = venues,userType=userType)

@app.route('/delete_notification/<path>/<id>',methods=['GET','POST'])
def delete_notification(path,id):
    id = int(id)
    current_user.deleteNotification(id)
    path = unquote_plus(path).strip("/")
    return redirect(path)

@app.route('/accept_notification/<path>/<id>',methods=['GET','POST'])
def accept_notification(path,id):
    id = int(id)
    notif = current_user.getNotification(id)
    event = ems.getEvent(notif.getEventId())
    event.setIsPending(False)
    current_user.addSession(event)
    current_user.deleteNotification(id)
    acceptNotification = DeletableNotification("{0} has accepted to be the presenter at '{1}' session".format(current_user.getName(),event.getName()))
    convener = event.getConvener()
    convener.addNotification(acceptNotification)
    seminar = ems.getEvent(event.getSeminarId())
    newSessionNotification = DeletableNotification("A new session '{0}' was added to '{1}' seminar".format(event.getName(),seminar.getName()))
    ems.notifyRegistrees(seminar.getId(),newSessionNotification)
    path = unquote_plus(path).strip("/")
    return redirect(path)

@app.route('/reject_notification/<path>/<id>',methods=['GET','POST'])
def reject_notification(path,id):
    id = int(id)
    notif = current_user.getNotification(id)
    event = ems.getEvent(notif.getEventId())
    ems.cancelEvent(event.getId()) 
    current_user.deleteNotification(id)
    rejectNotification = DeletableNotification("{0} has rejected to be presenter at '{1}' session".format(current_user.getName(),event.getName()))
    convener = event.getConvener()
    convener.addNotification(rejectNotification)
    path = unquote_plus(path).strip("/")
    return redirect(path)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('you were logged out')
    # set current user to unauthenticated
    return redirect(url_for('login'))