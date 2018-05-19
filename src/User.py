from src.Person import *
from flask_login import UserMixin
class User(UserMixin,Person):
    def __init__(self,name,zid,email,password):
        Person.__init__(self,name,email)
        self.__zid = zid
        self.__password = password
        self.__currEvents = {}
        self.__pastEvents = {}
        self.__notifications = {}
        self.isAuthenticated = False
        self.isActive = False
        self.isAnonymous = False
        self.__notifications[0] = "Welcome to the event management system " + name
    def getPassword(self):
        return self.__password
    def getCurrEvents(self):
        return self.__currEvents.values()
    def getPastEvents(self):
        return self.__pastEvents.values()
    def getNotificationsMap(self):
        return self.__notifications
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
            self.__currEvents[e.getId()] = e
    def setPastEvents(self,pastEvents):
        for e in pastEvents:
            self.__pastEvents[e.getId()] = e
        self.__pastEvents = pastEvents
    def addRegisteredEvent(self,event):
        if event.isOpen():
            self.__currEvents[event.getId()] = event
        else:
            self.__pastEvents[event.getId()] = event
    def removeRegisteredEvent(self,eventId):
        if eventId in self.__currEvents:
            del self.__currEvents[eventId]
            return True
        elif eventId in self.__pastEvents:
            del self.__pastEvents[eventId]
            return True
        return False
    def deleteNotification(self,id):
        if id in self.__notifications:
            del self.__notifications[id]
    def isRegistered(self,eventId):
        if eventId in self.__currEvents:
            return True
        if eventId in self.__pastEvents:
            return True
        return False
    def cancelRegisteredEvent(self,eventId):
        eventName = self.getRegisteredEventName(eventId)
        if self.removeRegisteredEvent(eventId):
            self.addNotification(eventName + " event was cancelled")
            return True
        return False
    def getUniqueNotificationID(self):
        id = 0
        while id in self.__notifications:
            id = id + 1
        return id
    def addNotification(self,notification):
        self.__notifications[self.getUniqueNotificationID()] = notification
    def getRegisteredEventName(self,id):
        if id in self.__currEvents:
            return self.__currEvents[id].getName()
        elif id in self.__pastEvents:
            return self.__pastEvents[id].getName()
        return None
    def getRegisteredEvent(self,eventId):
        if eventId in self.__currEvents:
            return self.__currEvents.get(eventId)
        if eventId in self.__pastEvents:
            return self.__pastEvents.get(eventId)
        return None