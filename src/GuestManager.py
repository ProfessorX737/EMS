from src.Staff import *
from src.Guest import *
from src.UserManager import *
from datetime import datetime

class GuestManager(UserManager):
    def __init__(self):
        self.__guest = {}
    def getUsers(self):
        return self.__guest.values()
    def setUsers(self,users):
        for u in users:
            self.__guest[u.get_id()] = u
    def addUser(self,name,zID,email,password,role):
        if zID not in self.__guest:
            guest = Guest(name,zID,email,password)
            self.__guest[guest.get_id()] = guest
            return True
        return False
    def getUserById(self,zid):
        if zid in self.__guest:
            return self.__guest.get(zid)
        else:
            return None
    def getUserByEmail(self,email):
        for user in self.__guest.values():
            if user.getEmail() == email:
                return user
        return None
    def getUserType(self):
        return "Guest"
    def addRegisteredEvent(self,userID,event):
        if userID in self.__guest:
            self.__guest[userID].addRegisteredEvent(event)
    def removeRegisteredEvent(self,userID,eventId):
        if userID in self.__guest:
            guest = self.__guest.get(userID)
            guest.removeRegisteredEvent(eventId)
    def cancelEvent(self,convener,eventId):
        for s in self.__guest.values():
            s.cancelRegisteredEvent(eventId)
        # convener.cancelPostedEvent(eventId)
    def notifyRegistreesNewSession(self,seminarId, seminarName, sessionName):
        for guest in self.__guest.values():
            if guest.isRegistered(seminarId):
                guest.addNotification("A new session '{0}' was added to '{1}' seminar".format(sessionName,seminarName))
    def notifyRegistreesEventEdit(self, eventId):
        for guest in self.__guest.values():
            if guest.isRegistered(eventId):
                guest.addNotification("The details of '{0}' event were changed".format(guest.getRegisteredEventName(eventId))) 
    def changeRegisteredEvent(self,oldEventId,editedEvent):
        for guest in self.__guest.values():
            if guest.isRegistered(oldEventId):
                guest.removeRegisteredEvent(oldEventId)
                guest.addRegisteredEvent(editedEvent)