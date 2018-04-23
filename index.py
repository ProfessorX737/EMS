from flask import Flask, render_template, url_for, flash, request, redirect, session
import os
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from UserManager import *
from EventManager import *
from Event import *
from Period import *
from Seminar import *
from Course import *
from EventManagementSystem import *
from CreateEventForm import *

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# userManager = UserManager()
# eventManager = EventManager()
ems = EventManagementSystem()

# startDateTime, endDateTime, name="",descr=""):
# (self,period,venue,convener,capacity,deregEnd):
# ems.addVenue("UNSW")
# e1 = Event(1,2,"coding 101","Learn how to code with xavier sensei","UNSW","Xavier",200,1.5)
# ems.entManager.addEvent(e1)
# startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd
@login_manager.user_loader
def loadUser(userName):
    return ems.getUser(userName)

with open('user.csv') as f:
    lines = f.readlines()
    for line in lines:
        attr = line.split(',')
        # remove new line character from last elt
        attr[-1] = attr[-1].strip()
        ems.addUser(attr[0],attr[1],attr[2],attr[3],attr[4])
        
@app.route('/',methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        zid = request.form.get('zid','')
        password = request.form.get('password','')
        user = loadUser(zid)
        if user is None or user.getPassword() != password:
            return redirect(url_for('index'))
        else:
            login_user(user)
            # Store user type globally after user logs in so we can keep track if they are Staff or Student
            global userType 
            userType = ems.getUserType(current_user.get_id())
            return redirect(url_for('home'))
    
    return render_template('login.html')

        
@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html',userType = userType,seminars = ems.getCurrentSeminars(), courses = ems.getCurrentCourses())
        
@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/create_event',methods=['GET','POST'])
def create_event():
    form = CreateEventForm()
    if form.validate_on_submit():
        if (form.eventType.data == 'Course'):
            ems.addCourse(str(form.startDateTime.data),str(form.endDateTime.data),
            form.name.data,form.description.data,form.venue.data,form.convener.data,
            form.capacity.data,str(form.deregEnd.data))
        # else: create seminar
    return render_template('create_event.html', form = form)

@app.route("/logout")
def logout():
    logout_user()
    flash('you were logged out')
    # set current user to unauthenticated
    return redirect(url_for('index'))
if __name__=='__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)


    # app.run()