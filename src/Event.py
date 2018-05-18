import datetime
from src.Period import *
from src.User import *
from src.exceptions.VenueCapacityException import *
import abc

class Event(Period):
    def __init__(self,id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,fee,earlybirdEnd):
        super().__init__(startDateTime,endDateTime,name,descr)
        self.__id = id
        self.__venue = venue
        self.__convener = convener
        self.__capacity = capacity
        self.__deregEnd = deregEnd
        self.__isCancelled = False
        self.__attendees = {}
        self.__fee = fee
        self.__earlybirdEnd = earlybirdEnd

    def addAttendee(self, user):
        if not self.isFull():
            self.__attendees[user.get_id()] = user
    def setAttendees(self, attendeeList):
        for attendee in attendeeList:
            self.__attendees[attendee.get_id()] = attendee
    def removeAttendee(self,userID):
        del self.__attendees[userID]

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
    
    @abc.abstractmethod
    def getClassName(self):
        pass


    