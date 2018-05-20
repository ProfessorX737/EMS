from src.Student import *
from src.Staff import *
from src.Guest import *
from abc import ABC
from datetime import datetime
class UserManager(ABC):
    def getUser(self):
        pass
    def setUser(self,students):
        pass
    def getCurrEvents(self,user):
        return user.getCurrEvents()
    def getPastEvents(self,user):
        return user.getPastEvents()
    def addUser(self,name,zID,email,password,role):
        pass
    def getUser(self,zid):
        pass
    def getUserType(self):
        pass
    def addRegisteredEvent(self,userID,event):
        pass
    def removeRegisteredEvent(self,userID,eventId):
        pass
    def cancelEvent(self,eventId):
        pass
    def notifyRegistrees(self,eventId,notification):
        pass
    def changeRegisteredEvent(self,oldEventId,editedEvent):
        pass