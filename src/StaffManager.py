from src.Staff import *
from src.Guest import *
from datetime import datetime
from src.UserManager import *
class StaffManager(UserManager):
    def __init__(self):
        super().__init__()
        
    def getUserType(self):
        return "Staff"
    def getPostedCurrEvents(self,staff):
        return staff.getPostedCurrEvents()
    def getPostedPastEvents(self,staff):
        return staff.getPostedPastEvents()
    def getCancelledEvents(self,staff):
        return staff.getCancelledEvents()
    def addUser(self,name,zID,email,password,role):
        user = Staff(name,zID,email,password)
        try:
            user = super().addUser(user)
            return user
        except UserExistsException as errMsg:
            raise errMsg
