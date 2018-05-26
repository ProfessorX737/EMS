from src.User import *
from src.Staff import *
from src.Guest import *
from src.exceptions.UserExistsException import *
from abc import ABC
from datetime import datetime
class UserManager(ABC):
    def __init__(self):
        self.__users = {}
    def getUsers(self):
        return self.__users.values()
    def setUsers(self,users):
        for u in users:
            self.__users[u.get_id()] = u
    def addUser(self,user):
        if user.get_id() in self.__users:
            raise UserExistsException("User","User with this userId already exists")
        elif self.getUserByEmail(user.getEmail()) is not None:
            raise UserExistsException("User","User with this email already exists")
        else:
            self.__users[user.get_id()] = user
           return user
    def getUserById(self,zid):
        if zid in self.__users:
            return self.__users.get(zid)
        else:
            return None
    def getUserByEmail(self,email):
        for user in self.__users.values():
            if user.getEmail() == email:
                return user
        return None
    def getUserType(self):
        pass
    def addRegisteredEvent(self,userID,event):
        if userID in self.__users:
            self.__users[userID].addRegisteredEvent(event)
    def removeRegisteredEvent(self,userID,eventId):
        if userID in self.__users:
            user = self.__users.get(userID)
            user.removeRegisteredEvent(eventId)
    def cancelEvent(self,eventId):
        for u in self.__users.values():
            u.cancelRegisteredEvent(eventId)
    def notifyRegistrees(self,eventId,notification):
        for user in self.__users.values():
            if user.isRegistered(eventId):
                user.addNotification(notification)
    def changeRegisteredEvent(self,oldEventId,editedEvent):
        for user in self.__users.values():
            if user.isRegistered(oldEventId):
                user.removeRegisteredEvent(oldEventId)
                user.addRegisteredEvent(editedEvent)