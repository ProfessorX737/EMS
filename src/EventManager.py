import datetime
from src.Seminar import *
class EventManager:
    def __init__(self):
        self.__events = {}
    def getEvents(self):
        return self.__events.values()
    def deregisterUser(self,eventId,userID):
        self.__events.get(eventId).removeAttendee(userID)
    def registerUser(self,eventId,user):
        self.__events.get(eventId).addAttendee(user)
    def getEvent(self,eventId):
        return self.__events.get(eventId)
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
    def cancelEvent(self,eventId):
        if eventId in self.__events:
            self.__events.get(eventId).cancelEvent()
            return True
        return False
    def refreshEvents(self,user):
        currentEvents = user.getCurrentEvents()
        pastEvents = user.getPastEvents()
        for event in currentEvents:
            if not event.isOpen():
                pastEvents.append(event)
                currentEvents.remove(event)
    def addEvent(self, event):
        if (event.getName() not in self.__events and
          event.getCapacity() <= event.getVenueName().getMaxCapacity()):
            self.__events[event.getName()] = event
        if event.getId() not in self.__events:
            self.__events[event.getId()] = event
            return True
        return False
    def deleteEvent(self,eventId):
        if eventId in self.__events:
            del self.__events[eventId]
    def containsEventId(self,id):
        if id in self.__events:
            return True
        return False
