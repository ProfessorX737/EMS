from flask import Flask, render_template, url_for, flash, request, redirect, session
import os
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from UserManager import *
from EventManager import *
from Event import *
from Period import *
from Seminar import *
from Course import *

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

userManager = UserManager()
eventManager = EventManager()

userType = ""

# startDateTime, endDateTime, name="",descr=""):
# (self,period,venue,convener,capacity,deregEnd):
eventManager.addVenue("UNSW")
e1 = Event(1,2,"coding 101","Learn how to code with xavier sensei","UNSW","Xavier",200,1.5)
eventManager.addEvent(e1)
# startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd
@login_manager.user_loader
def loadUser(userName):
    return userManager.getUser(userName)

with open('user.csv') as f:
    lines = f.readlines()
    for line in lines:
        attr = line.split(',')
        # remove new line character from last elt
        attr[-1] = attr[-1].strip()
        userManager.addUser(attr[0],attr[1],attr[2],attr[3],attr[4])
        
@app.route('/',methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        zid = request.form.get('zid','')
        password = request.form.get('password','')
        userType = userManager.getUserType(current_user.get_id())
        user = loadUser(zid)
        if user is None or user.getPassword() != password:
            return redirect(url_for('index'))
        else:
            login_user(user)
            return redirect(url_for('home'))
    
    return render_template('login.html')

        
@app.route('/home',methods=['GET','POST'])
def home():
    # Must update events first.
    # Sort events into courses and seminars 
    courses = []
    seminars = []
    for e in eventManager.getEvents():
        if isinstance(e,Seminar):
            seminars.append(e)
        elif isinstance(e,Course):
            courses.append(e)

    return render_template('home.html',seminars = seminars, courses = courses)
        
@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')

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