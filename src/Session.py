from src.Event import Event
from src.Period import *

# class Session(Period):
#     def __init__(self,id,startDateTime,endDateTime,name,descr,presenter):
#         super().__init__(startDateTime,endDateTime,name,descr)                   # period
#         self.__presenter = presenter           # Person
#         self.__id = id
    
#     def getId(self):
#         return self.__id
    
#     def getPresenter(self):
#         return self.__presenter

#     def setPresenter(self,presenter):
#         self.__presenter = presenter

class Session(Event):
    def __init__(self,seminarId,sessionId,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,presenter):
        super().__init__(sessionId,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd)
        self.__seminarId = seminarId           # Integer
        self.__presenter = presenter           # Guest
    
    def getPresenter(self):
        return self.__presenter
    def getSeminarId(self):
        return self.__seminarId

    def setPresenter(self,presenter):
        self.__presenter = presenter
    
    def getClassName(self):
        return "Session"