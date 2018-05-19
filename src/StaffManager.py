from src.Staff import *
from src.Guest import *
from datetime import datetime
from src.UserManager import *
class StaffManager(UserManager):
    def __init__(self):
        self.__staff = {}
    def getUsers(self):
        return self.__staff.values()
    def setUsers(self,users):
        for u in users:
            self.__staff[u.get_id()] = u
    def addUser(self,name,zID,email,password,role):
        if zID not in self.__staff:
            staff = Staff(name,zID,email,password)
            self.__staff[staff.get_id()] = staff
            return True
        return False
    def getUserById(self,zid):
        if zid in self.__staff:
            return self.__staff.get(zid)
        else:
            return None
    def getUserByEmail(self,email):
        for user in self.__staff.values():
            if user.getEmail() == email:
                return user
        return None
    def getUserType(self):
        return "Staff"
    def addRegisteredEvent(self,userID,event):
        if userID in self.__staff:
            self.__staff[userID].addRegisteredEvent(event)
    def removeRegisteredEvent(self,userID,eventId):
        if userID in self.__staff:
            staff = self.__staff.get(userID)
            staff.removeRegisteredEvent(eventId)
    def cancelEvent(self,convener,eventId):
        for s in self.__staff.values():
            s.cancelRegisteredEvent(eventId)
        # convener.cancelPostedEvent(eventId)
    def notifyRegistreesNewSession(self,seminarId, seminarName, sessionName):
        for staff in self.__staff.values():
            if staff.isRegistered(seminarId):
                staff.addNotification("A new session '{0}' was added to '{1}' seminar".format(sessionName,seminarName))
    def notifyRegistreesEventEdit(self, eventId):
        for staff in self.__staff.values():
            if staff.isRegistered(eventId):
                staff.addNotification("The details of '{0}' event were changed".format(staff.getRegisteredEventName(eventId))) 
    def changeRegisteredEvent(self,oldEventId,editedEvent):
        for staff in self.__staff.values():
            if staff.isRegistered(oldEventId):
                staff.removeRegisteredEvent(oldEventId)
                staff.addRegisteredEvent(editedEvent)
    def getPostedCurrEvents(self,staff):
        return staff.getPostedCurrEvents()
    def getPostedPastEvents(self,staff):
        return staff.getPostedPastEvents()
    def getCancelledEvents(self,staff):
        return staff.getCancelledEvents()