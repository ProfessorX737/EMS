import time
from Period import Period

class Event:
    def __init__(self,period,capacity,deregPeriod):
        self._period = period
        self._capacity = capacity
        self._deregPeriod = deregPeriod
        self._isCancelled = False
        self._attendees = []
    
    def getPeriod(self):
        return self._period
    def getCapacity(self):
        return self._capacity
    def getDeregPeriod(self):
        return self._deregPeriod
    def getAttendees(self):
        retrun self._attendees

    # should another use case be "As a Staff, I want to change the details of an event"
    # As a registered user to an event, I want to be notified if important details of an event change
    def setPeriod(self, period):
        self._period = period
    def setCapacity(self,capacity):
        self._capacity = capacity
    def setDeregPeriod(self,deregPeriod):
        self._deregPeriod = deregPeriod

    def isCancelled(self):
        return self._isCancelled
    def isOpen(self):
        self._period.get
        localTime = time.localtime(time.time())
        localTime.

    