import datetime
from Period import *
from User import *
import abc

class Event(Period):
    def __init__(self,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd):
        super().__init__(startDateTime,endDateTime,name,descr)
        self.__venue = venue
        self.__convener = convener
        self.__capacity = capacity
        self.__deregEnd = deregEnd
        self.__isCancelled = False
        self.__attendees = {}

    def addAttendee(self,user):
        if not self.isFull():
            self.__attendees[user.get_id()] = user
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
    def cancelEvent(self):
        self.__isCancelled = True

    @abc.abstractmethod
    def getClassName(self):
        pass


    