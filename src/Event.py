import datetime
from src.Period import *
from src.User import *
import abc

class Event:
    def __init__(self,id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd):
        self.__id = id
        self.__venue = venue
        self.__convener = convener
        self.__capacity = capacity
        self.__deregEnd = deregEnd
        self.__isCancelled = False
        self.__attendees = {}
        self.__name = name                     # String
        self.__descr = descr                   # String
        self.__startDateTime = startDateTime   # datetime
        self.__endDateTime = endDateTime       # datetime
    
    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__descr
    def getStartDateTime(self):
        return self.__startDateTime
    def getEndDateTime(self):
        return self.__endDateTime

    def setName(self, name):
        self.__name = name
    def setDescription(self, descr):
        self.__descr = descr
    def setStartDateTime(self, startDateTime):
        self.__startDateTime = startDateTime
    def setEndDateTime(self, endDateTime):
        self.__endDateTime = endDateTime

    def addAttendee(self, user):
        if not self.isFull():
            self.__attendees[user.get_id()] = user
    def setAttendees(self, attendeeList):
        for attendee in attendeeList:
            self.__attendees[attendee.get_id()] = attendee
    def removeAttendee(self,userID):
        if userID in self.__attendees:
            del self.__attendees[userID]
    def hasAttendee(self,userID):
        if userID in self.__attendees:
            return True
        return False

    def isCancelled(self):
        return self.__isCancelled
    def isOpen(self):
        if self.getEndDateTime() < datetime.datetime.now() or self.__isCancelled:
            return False
        else:
            return True
    def isFull(self):
        if len(self.__attendees.values()) >= self.__capacity:
            return True
        return False
    
    def getId(self):
        return self.__id
    def getConvener(self):
        return self.__convener
    def getVenueName(self):
        return self.__venue
    def getCapacity(self):
        return self.__capacity
    def getDeregEnd(self):
        return self.__deregEnd
    def getAttendees(self):
        return self.__attendees.values()
    def getNumAttendees(self):
        return len(self.__attendees.values())

    def setCapacity(self,capacity):
        self.__capacity = capacity
    def setDeregEnd(self,deregEnd):
        self.__deregEnd = deregEnd
    def setVenue(self, venue):
        self.__venue = venue
    def setConvener(self, convenerName):
        self.__convener = convenerName
    def cancelEvent(self):
        self.__isCancelled = True

    @abc.abstractmethod
    def getClassName(self):
        pass


    