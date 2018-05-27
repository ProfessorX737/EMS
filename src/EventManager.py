import datetime
from src.Seminar import *
from src.exceptions.InvalidEventDateException import *
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
    def cancelPeriod(self,eventId):
        event = self.getEvent(eventId)
        venue = event.getVenue()
        venue.deletePeriod(eventId)
    def cancelEvent(self,eventId):
        if eventId in self.__events:
            self.__events.get(eventId).cancelEvent()
            self.cancelPeriod(eventId)
            return True
        return False
    def refreshEvents(self,user):
        currentEvents = user.getCurrentEvents()
        pastEvents = user.getPastEvents()
        for event in currentEvents:
            if not event.isOpen():
                pastEvents.append(event)
                currentEvents.remove(event)
    def containsEventName(self,eventName):
        for e in self.getEvents():
            if e.getName() == eventName and not e.isCancelled():
                return True
        return False
    def addEvent(self, event):
        print("start date time is ",event.getStartDateTime(),datetime.datetime.now())
        if event.getStartDateTime() < datetime.datetime.now():
            print("here")
            raise InvalidEventDateException('StartDateTime','StartDateTime >= Current Date Time')
        if event.getId() not in self.__events and not self.containsEventName(event.getName()):
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
    def getCost(self,eventId):
        if eventId in self.__events:
            event = self.__events[eventId]
            return event.getFee()
        return None
