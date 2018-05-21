import datetime
#from Venue import Venue

class Period:
    def __init__(self,startDateTime,endDateTime,id):
    #    self.__name = name                     # String
    #    self.__descr = descr                   # String
        self.__id = id
        self.__startDateTime = startDateTime   # datetime
        self.__endDateTime = endDateTime       # datetime
    
    def getId(self):
        return self.__id
    def getStartDateTime(self):
        return self.__startDateTime
    def getEndDateTime(self):
        return self.__endDateTime

    def setId(self,id):
        self.__id = id
    def setStartDateTime(self, startDateTime):
        self.__startDateTime = startDateTime
    def setEndDateTime(self, endDateTime):
        self.__endDateTime = endDateTime