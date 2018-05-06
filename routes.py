from flask import Flask, render_template, url_for, flash, request, redirect, session
import os
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from src.UserManager import *
from src.EventManager import *
from src.Event import *
from src.Period import *
from src.Seminar import *
from src.Course import *
from src.CreateEventForm import *
from src.CreateSessionForm import *
from src.CreateVenueForm import *
from Server import app, ems, loadUser

with open('user.csv') as f:
    lines = f.readlines()
    for line in lines:
        attr = line.split(',')
        # remove new line character from last elt
        attr[-1] = attr[-1].strip()
        ems.addUser(attr[0],attr[1],attr[2],attr[3],attr[4])
        
@app.route('/',methods=['GET','POST'])
def login():
    if (request.method == 'POST'):
        zid = request.form.get('zid','')
        password = request.form.get('password','')
        user = loadUser(zid)
        if user is None or user.getPassword() != password:
            return redirect(url_for('login'))
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
    # form = CreateEventForm()
    venueNames = ems.getVenueNames()
    form = NewStartUpForm(venueNames).getForm()
    if form.validate_on_submit():
        if (form.eventType.data == 'Course'):
            ems.addCourse(current_user,form.startDateTime.data,form.endDateTime.data,
            form.name.data,form.description.data,form.venue.data,form.convener.data,
            form.capacity.data,form.deregEnd.data)
        else:
            ems.addSeminar(current_user,form.startDateTime.data,form.endDateTime.data,
            form.name.data,form.description.data,form.venue.data,form.convener.data,
            form.capacity.data,form.deregEnd.data)
        return redirect(url_for('home'))
    return render_template('create_event.html', form = form, userType=userType)

@app.route("/more/<eventType>/<eventName>",methods=['GET','POST'])
@login_required        
def moreInfo(eventType,eventName):
    event = ems.getEvent(eventName)
    isOwner = ems.isMyEvent(current_user.get_id(),eventName)
    # if staff check if this event is inside getPostedCurrEvents
    return render_template('more_info.html',isOwner=isOwner,event=event,userType=userType)

@app.route('/create_session/<seminarName>',methods=['GET','POST'])
@login_required        
def create_session(seminarName):
    form = CreateSessionForm()
    if form.validate_on_submit():
        ems.addSession(seminarName,form.startDateTime.data,form.endDateTime.data,
        form.name.data,form.description.data,form.convener.data)
        return redirect(url_for('moreInfo',eventType='Seminar',eventName=seminarName))
    return render_template('create_session.html',seminarName=seminarName,form=form,userType=userType)

@app.route('/register/<eventName>',methods=['GET','POST'])
@login_required        
def register_user(eventName):
    event = ems.getEvent(eventName)
    ems.addRegisteredEvent(current_user.get_id(),event)
    if isinstance(event,Course):
        ems.registerUserToCourse(eventName,current_user)
    if isinstance(event,Seminar):
        ems.registerUserToSeminar(eventName,current_user)
    return redirect(url_for('moreInfo',eventType=event.getClassName(),eventName=eventName))

@app.route('/deregister/<eventName>',methods=['GET','POST'])
@login_required        
def deregister_user(eventName):
    event = ems.getEvent(eventName)
    ems.removeRegisteredEvent(current_user.get_id(),eventName)
    if isinstance(event,Course):
        ems.deregisterUserFromCourse(eventName,current_user.get_id())
    if isinstance(event,Seminar):
        ems.deregisterUserFromSeminar(eventName,current_user.get_id())
    return redirect(url_for('moreInfo',eventType=event.getClassName(),eventName=eventName))

@app.route('/edit_event/<eventName>',methods=['GET','POST'])
@login_required        
def edit_event(eventName):
    event = ems.getEvent(eventName)

    venueNames = ems.getVenueNames()
    form = NewStartUpForm(venueNames).getForm()
    form.fillDefault(event)

    if form.validate_on_submit():
        ems.deleteEvent(event)
        if (isinstance(event,Course)):
            ems.addCourse(current_user,form.startDateTime.data,form.endDateTime.data,
            form.name.data,form.description.data,form.venue.data,form.convener.data,
            form.capacity.data,form.deregEnd.data)
        else:
            ems.addSeminar(current_user,form.startDateTime.data,form.endDateTime.data,
            form.name.data,form.description.data,form.venue.data,form.convener.data,
            form.capacity.data,form.deregEnd.data)
        return redirect(url_for('home'))
    return render_template('edit_event.html',form=form,event=event)

@app.route('/cancel_event/<eventName>',methods=['GET','POST'])
@login_required        
def cancel_event(eventName):
    ems.cancelEvent(current_user,eventName)
    return redirect(url_for('home'))

@app.route('/delete_venue/<venueName>',methods=['GET','POST'])
@login_required        
def delete_venue(venueName):
    ems.removeVenue(venueName)
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