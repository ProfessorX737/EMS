from src.Event import Event
from src.Period import *

class Session(Event):
    def __init__(self,seminarId,sessionId,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,presenter):
        super().__init__(sessionId,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd)
        self.__seminarId = seminarId           # Integer
        self.__presenter = presenter           # Guest
    
    def getPresenter(self):
        return self.__presenter
    def getPresenterName(self):
        return self.__presenter.getName()
    def getPresenterId(self):
        return self.__presenter.get_id()
    def getSeminarId(self):
        return self.__seminarId

    def setPresenter(self,presenter):
        self.__presenter = presenter
    
    def getClassName(self):
        return "Session"