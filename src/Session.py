from src.Event import Event
from src.Period import *

class Session(Event):
    def __init__(self,seminarId,sessionId,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,presenter,fee,earlybird):
        super().__init__(sessionId,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,fee,earlybird)
        self.__seminarId = seminarId           # Integer
        self.__presenter = presenter           # Guest
        self.__isPending = True
    
    def getPresenter(self):
        return self.__presenter
    def getPresenterName(self):
        return self.__presenter.getName()
    def getPresenterId(self):
        return self.__presenter.get_id()
    def getSeminarId(self):
        return self.__seminarId
    def getIsPending(self):
        return self.__isPending
    def setIdPending(self, isPending):
        self.__isPending = isPending
    def setPresenter(self,presenter):
        self.__presenter = presenter
    def getClassName(self):
        return "Session"
