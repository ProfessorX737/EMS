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
from Server import app, ems, loadUser

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
        user = loadUser(zid)
        if user is None:
            return render_template('login.html',message= "'{0}'".format(zid) + " is not a valid username")
        if user.getPassword() != password:
            return render_template('login.html',message="Incorrect password")
        else:
            login_user(user)
            # Store user type globally after user logs in so we can keep track if they are Staff or Student
            global userType 
            userType = ems.getUserType(current_user.get_id())
            return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/home',methods=['GET','POST'])
@login_required        
def home():
    return render_template('home.html',userType = userType,seminars = ems.getCurrentSeminars(), courses = ems.getCurrentCourses())

@app.route('/dashboard',methods=['GET','POST'])
@login_required        
def dashboard():
    return render_template('dashboard.html',userType=userType)

@app.route('/create_event',methods=['GET','POST'])
@login_required        
def create_event():   
    venueNames = ems.getVenueNames()
    form = NewStartUpForm(venueNames).getForm()
    message = ''
    if form.validate_on_submit():
        if (form.eventType.data == 'Course'):
            if (ems.addCourse(current_user,form.startDateTime.data,form.endDateTime.data,
            form.name.data,form.description.data,form.venue.data,form.convener.data,
            form.capacity.data,form.deregEnd.data)):
                return redirect(url_for('home'))
            else:
                message = 'Course name already taken'
        else:
            if(ems.addSeminar(current_user,form.startDateTime.data,form.endDateTime.data,
            form.name.data,form.description.data,form.venue.data,form.convener.data,
            form.capacity.data,form.deregEnd.data)):
                return redirect(url_for('home'))
            else:
                message = 'Seminar name already taken'

    return render_template('create_event.html', form = form, userType=userType, message=message)

@app.route("/more/<eventType>/<eventId>",methods=['GET','POST'])
@login_required        
def moreInfo(eventType,eventId):
    event = ems.getEvent(eventId)
    isOwner = ems.isMyEvent(current_user.get_id(),eventId)
    # if staff check if this event is inside getPostedCurrEvents
    return render_template('more_info.html',isOwner=isOwner,event=event,userType=userType)

@app.route('/create_session/<seminarId>',methods=['GET','POST'])
@login_required        
def create_session(seminarId):
    form = CreateSessionForm()
    if form.validate_on_submit():
        ems.addSession(seminarId,form.startDateTime.data,form.endDateTime.data,
        form.name.data,form.description.data,form.convener.data)
        return redirect(url_for('moreInfo',eventType='Seminar',eventId=seminarId))
    return render_template('create_session.html',seminarId=seminarId,form=form,userType=userType)

@app.route('/register/<eventId>',methods=['GET','POST'])
@login_required        
def register_user(eventId):
    event = ems.getEvent(eventId)
    print("current user id " + current_user.get_id())
    ems.addRegisteredEvent(current_user.get_id(),event)
    if isinstance(event,Course):
        ems.registerUserToCourse(eventId,copy.copy(current_user))
    if isinstance(event,Seminar):
        ems.registerUserToSeminar(eventId,copy.copy(current_user))
    return redirect(url_for('moreInfo',eventType=event.getClassName(),eventId=eventId))

@app.route('/deregister/<eventId>',methods=['GET','POST'])
@login_required        
def deregister_user(eventId):
    event = ems.getEvent(eventId)
    ems.removeRegisteredEvent(current_user.get_id(),eventId)
    if isinstance(event,Course):
        ems.deregisterUserFromCourse(eventId,current_user.get_id())
    if isinstance(event,Seminar):
        ems.deregisterUserFromSeminar(eventId,current_user.get_id())
    return redirect(url_for('moreInfo',eventType=event.getClassName(),eventId=eventId))

@app.route('/edit_event/<eventId>',methods=['GET','POST'])
@login_required        
def edit_event(eventId):
    event = ems.getEvent(eventId)
    venueNames = ems.getVenueNames()
    form = NewStartUpForm(venueNames).getForm()
    form.fillDefault(event)
    message=''
    attendees = event.getAttendees()
    oldEventId = event.getId()
    if form.validate_on_submit():
        # ems.deleteEvent(oldEventId)
        if (event.getNumAttendees() > form.capacity.data):
            message='new capacity must be >= current number of attendees'
            return render_template('edit_event.html',form=form,event=event,message=message)
        event.setStartDateTime(form.startDateTime.data)
        event.setEndDateTime(form.endDateTime.data)
        event.setName(form.name.data)
        event.setDescription(form.description.data)
        event.setVenue(form.venue.data)
        event.setConvener(form.convener.data)
        event.setCapacity(form.capacity.data)
        event.setDeregEnd(form.deregEnd.data)
        # if (isinstance(event,Course)):
        #     ems.addCourse(current_user,form.startDateTime.data,form.endDateTime.data,
        #     form.name.data,form.description.data,form.venue.data,form.convener.data,
        #     form.capacity.data,form.deregEnd.data)
        # else:
        #     ems.addSeminar(current_user,form.startDateTime.data,form.endDateTime.data,
        #     form.name.data,form.description.data,form.venue.data,form.convener.data,
        #     form.capacity.data,form.deregEnd.data)
        # editedEvent = ems.getEvent(form.name.data)
        # ems.changeRegisteredEvent(oldEventName,attendees,editedEvent)
        return redirect(url_for('home'))
    return render_template('edit_event.html',form=form,event=event,message=message)

@app.route('/cancel_event/<eventId>',methods=['GET','POST'])
@login_required        
def cancel_event(eventId):
    ems.cancelEvent(current_user,eventId)
    return redirect(url_for('home'))

@app.route('/delete_venue/<venueId>',methods=['GET','POST'])
@login_required        
def delete_venue(venueId):
    ems.removeVenue(venueId)
    return redirect(url_for('view_venues'))

@app.route('/create_venue',methods=['GET','POST'])
@login_required        
def create_venue():
    form = CreateVenueForm()
    if form.validate_on_submit():
        ems.addVenue(form.name.data,form.location.data,form.capacity.data)
        return redirect(url_for('view_venues'))
    return render_template('create_venue.html',form=form,userType=userType)

@app.route('/venues',methods=['GET','POST'])
@login_required        
def view_venues():
    venues = ems.getVenues()
    return render_template('venues.html',venues = venues,userType=userType)

@app.route('/delete_notification/<path>/<id>',methods=['GET','POST'])
def delete_notification(path,id):
    current_user.deleteNotification(int(id))
    return redirect(url_for(path))

@app.route("/logout")
@login_required        
def logout():
    logout_user()
    flash('you were logged out')
    # set current user to unauthenticated
    return redirect(url_for('login'))