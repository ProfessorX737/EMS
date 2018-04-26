from Person import *
from flask_login import UserMixin
class User(UserMixin,Person):
    def __init__(self,name,zid,email,password):
        Person.__init__(self,name,email)
        self.__zid = zid
        self.__password = password
        self.__currEvents = {}
        self.__pastEvents = {}
        self.isAuthenticated = False
        self.isActive = False
        self.isAnonymous = False
    def getPassword(self):
        return self.__password
    def getCurrEvents(self):
        return self.__currEvents.values()
    def getPastEvents(self):
        return self.__pastEvents.values()
    # Flask login module required functions
    def get_id(self):
        return self.__zid
    def setName(self,name):
        self.__name = name
    def setId(self,zid):
        self.__zid = zid
    def setEmail(self,email):
        self.__email = email
    def setPassword(self,password):
        self.__password = password
    def setCurrEvents(self,currEvents):
        for e in currEvents:
            self.__currEvents[e.getName()] = e
    def setPastEvents(self,pastEvents):
        for e in pastEvents:
            self.__pastEvents[e.getName()] = e
        self.__pastEvents = pastEvents
    def addRegisteredEvent(self,event):
        if event.isOpen():
            self.__currEvents[event.getName()] = event
        else:
            self.__pastEvents[event.getName()] = event
    def removeRegisteredEvent(self,eventName):
        del self.__currEvents[eventName]
        del self.__pastEvents[eventName]
    def isRegistered(self,eventName):
        if eventName in self.__currEvents:
            return True
        if eventName in self.__pastEvents:
            return True
        return False