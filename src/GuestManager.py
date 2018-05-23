from src.Staff import *
from src.Guest import *
from src.UserManager import *
from datetime import datetime

class GuestManager(UserManager):
    def __init__(self):
        super().__init__()
    def addUser(self,name,zID,email,password,role):
        if zID not in self.__users:
            user = Guest(name,zID,email,password)
            self.__users[user.get_id()] = user
            return True
    def getUserType(self):
        return "Guest"
