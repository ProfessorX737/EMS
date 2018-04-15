import datetime
#from Venue import Venue

class Period:
    def __init__(self,startDateTime, endDateTime, name="",descr=""):
        self.__name = name                     # String
        self.__descr = descr                   # String
        self.__startDateTime = startDateTime   # datetime
        self.__endDateTime = endDateTime       # datetime

    @classmethod
    def copy(cls,period):
        cls.name = period.getName()
        cls.descr = period.getDescription()
        cls.startDateTime = period.getStartDateTime()
        cls.endDateTime = period.getEndDateTime()
        return cls(cls.startDateTime,cls.endDateTime,cls.name,cls.descr)
    
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