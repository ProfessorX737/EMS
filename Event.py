import datetime
from Period import *
from User import *

class Event(Period):
    def __init__(self,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd):
        super().__init__(startDateTime,endDateTime,name,descr)
        self.__venue = venue
        self.__convener = convener
        self.__capacity = capacity
        self.__deregEnd = deregEnd
        self.__isCancelled = False
        self.__attendees = {}

    def addAttendee(self,attendee):
        if not isinstance(attendee,User):
            return False
        if not self.isFull():
            self.__attendees[attendee.getName()] = attendee
            return True
        return False
    def removeAttendee(self,attendeeName):
        del self.__attendees[attendeeName]

    def isCancelled(self):
        return self.__isCancelled
    def isOpen(self):
        return self.__endDateTime < datetime.datetime.now()
    def isFull(self):
        if len(self.__attendees) >= self.__capacity:
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
        return self.__attendees
    def getNumAttendees(self):
        return len(self.__attendees)

    def setCapacity(self,capacity):
        self.__capacity = capacity
    def setDeregEnd(self,deregEnd):
        self.__deregEnd = deregEnd
    def setVenue(self, venue):
        self.__venue = venue
    def cancelEvent(self):
        self.__isCancelled = True


    