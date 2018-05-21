import datetime
from src.Period import *
from src.User import *
from src.exceptions.VenueCapacityException import *
from src.Period import *
import abc

class Event:
    def __init__(self,eventId,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,fee,earlybirdEnd):
        self.__id = eventId
        # self.__periodId = periodId
        self.__period = Period(startDateTime,endDateTime,eventId)
        self.__venue = venue
        self.__convener = convener
        self.__capacity = capacity
        self.__deregEnd = deregEnd
        self.__isCancelled = False
        self.__attendees = {}
        self.__name = name                     # String
        self.__descr = descr                   # String
        # self.__startDateTime = startDateTime   # datetime
        # self.__endDateTime = endDateTime       # datetime
        self.__fee = fee
        self.__earlybirdEnd = earlybirdEnd
        venue.addPeriod(self.__period)

    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__descr
    def getStartDateTime(self):
        return self.__period.getStartDateTime()
    def getEndDateTime(self):
        return self.__period.getEndDateTime()
    def getPeriodId(self):
        return self.__period.getId()
    def setName(self, name):
        self.__name = name
    def setDescription(self, descr):
        self.__descr = descr
    def setStartDateTime(self, startDateTime):
        self.__period.setStartDateTime(startDateTime)
    def setEndDateTime(self, endDateTime):
        self.__period.setEndDateTime(endDateTime)

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
    def getConvenerName(self):
        return self.__convener.getName()
    def getVenue(self):
        return self.__venue
    def getVenueId(self):
        return self.__venue.getId()
    def getVenueName(self):
        return self.__venue.getName()
    def getCapacity(self):
        return self.__capacity
    def getDeregEnd(self):
        return self.__deregEnd
    def getAttendees(self):
        return self.__attendees.values()
    def getNumAttendees(self):
        return len(self.__attendees.values())
    def getEarlyBirdEnd(self):
        return self.__earlybirdEnd
    def getCost(self):
        if datetime.datetime.now() > self.__earlybirdEnd:
            return self.__fee
        else:
            return 0.5*self.__fee
    def getFee(self):
        return self.__fee
    def setCapacity(self,capacity):
        if capacity > self.__venue.getMaxCapacity():
            raise VenueCapacityException('Capacity','New event capacity > Venue capacity')
        else:
            self.__capacity = capacity
    def setDeregEnd(self,deregEnd):
        self.__deregEnd = deregEnd
    def setVenue(self, venue):
        self.__venue = venue
    def setConvener(self, convenerName):
        self.__convener = convenerName
    def setEarlyBirdEnd(self, earlybirdEnd):
        self.__earlybirdEnd = earlybirdEnd
    def setFee(self,fee):
        self.__fee = fee
    def cancelEvent(self):
        self.__isCancelled = True
    def getStatus(self):
        if self.isOpen():
            return "Open"
        elif self.isCancelled():
            return "Cancelled"
        else:
            return "Closed"

    @abc.abstractmethod
    def getClassName(self):
        pass


    