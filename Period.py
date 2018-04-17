import datetime
#from Venue import Venue

class Period:
    def __init__(self,startDateTime, endDateTime, name="",descr=""):
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