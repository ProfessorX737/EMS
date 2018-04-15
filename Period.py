import datetime
#from Venue import Venue

class Period:
    def __init__(self, name, descr, startDateTime, endDateTime):
        self._name = name                     # String
        self._descr = descr                   # String
        self._startDateTime = startDateTime   # datetime
        self._endDateTime = endDateTime       # datetime

    @classmethod
    def copy(cls,period):
        cls.name = period.getName()
        cls.descr = period.getDescription()
        cls.startDateTime = period.getStartDateTime
        cls.endDateTime = period.getEndDateTime
        return cls(cls.name,cls.descr,cls.startDateTime,cls.endDateTime)
    
    def getName(self):
        return self._name
    def getDescription(self):
        return self._descr
    def getStartDateTime(self):
        return self._startDateTime
    def getEndDateTime(self):
        return self._endDateTime

    def setName(self, name):
        self._name = name
    def setDescription(self, descr):
        self._descr = descr
    def setStartDateTime(self, startDateTime):
        self._startDateTime = startDateTime
    def setEndDateTime(self, endDateTime):
        self._endDateTime = endDateTime