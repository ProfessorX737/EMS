import datetime
from Seminar import *
class EventManager:
    def __init__(self):
        self.__events = {}
    def getEvents(self):
        return self.__events.values()
    def deregisterUser(self,eventName,userName):
        self.__events.get(eventName).removeAttendee(userName)
    def registerUser(self,eventName,user):
        self.__events.get(eventName).addAttendee(user)
    def getEvent(self,eventName):
        return self.__events.get(eventName)
    def getPastEvents(self):
        pastEvents = []
        for event in self.__events.values():
            if not event.isOpen():
                pastEvents.append(event)
        return pastEvents
    def getCurrentEvents(self):
        currentEvents = []
        for event in self.__events.values():
            if event.isOpen():
                currentEvents.append(event)
        return currentEvents
    def cancelEvent(self,eventName):
        self.__events.get(eventName).cancelEvent()
    def refreshEvents(self,user):
        currentEvents = user.getCurrentEvents()
        pastEvents = user.getPastEvents()
        for event in currentEvents:
            if not event.isOpen():
                pastEvents.append(event) 
                currentEvents.remove(event)
    def addEvent(self, event):
        self.__events[event.getName()] = event
    def parseDateTime(self,dateTimeString):
        return datetime.datetime.strptime(dateTimeString,"%d-%m-%Y %H:%M")
