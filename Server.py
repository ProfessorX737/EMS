from flask import Flask, render_template, url_for, flash, request, redirect, session
import os
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from src.EventManagementSystem import *
from src.exceptions.LoginException import *

app = Flask(__name__)
app.secret_key = 'itsasecret'
app.config['TESTING'] = False
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

ems = EventManagementSystem()

@login_manager.user_loader
def loadUser(userName):
    try:
        user = ems.getUserById(userName)
    except LoginException:
        return None
    else:
        return user
     