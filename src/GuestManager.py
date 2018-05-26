from src.Staff import *
from src.Guest import *
from src.UserManager import *
from datetime import datetime

class GuestManager(UserManager):
    def __init__(self):
        super().__init__()
    def addUser(self,name,userId,email,password,role):
        user = Guest(name,userId,email,password)
        super().addUser(user)
    def getUserType(self):
        return "Guest"
