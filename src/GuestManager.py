from src.Staff import *
from src.Guest import *
from src.UserManager import *
from datetime import datetime

class GuestManager(UserManager):
    def __init__(self):
        super().__init__()
    def addUser(self,name,zID,email,password,role):
        user = Guest(name,zID,email,password)
        try:
            user = super().addUser(user)
            return user
        except UserExistsException as errMsg:
            raise errMsg
    def getUserType(self):
        return "Guest"
