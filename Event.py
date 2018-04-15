import datetime
from Period import Period

class Event(Period):
    def __init__(self,period,venue,convener,capacity,deregEnd):
        super().copy(period)
        self._venue = venue
        self._convener = convener
        self._capacity = capacity
        self._deregEnd = deregEnd
        self._isCancelled = False
        self._attendees = []

    def addAttendee(self,attendee):
        if not isinstance(attendee,User):
            return False
        if not self.isFull():
            self._attendees.append(attendee)
            return True
        return False

    def isCancelled(self):
        return self._isCancelled
    def isOpen(self):
        return self._endDateTime < datetime.datetime.now()  
    def isFull(self):
        if len(self._attendees) >= self._capacity:
            return True
        return False
    
    def getConvener(self):
        return self._convener
    def getVenue(self):
        return self._venue
    def getCapacity(self):
        return self._capacity
    def getDeregEnd(self):
        return self._deregEnd
    def getAttendees(self):
        return self._attendees

    def setCapacity(self,capacity):
        self._capacity = capacity
    def setDeregEnd(self,deregEnd):
        self._deregEnd = deregEnd
    def setVenue(self, venue):
        self._venue = venue
    def cancelEvent(self):
        self._isCancelled = True


    