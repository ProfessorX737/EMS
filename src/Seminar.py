from src.Event import Event
from src.Session import Session

class Seminar(Event):
    def __init__(self,id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd):
        super().__init__(id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd)
        self.__sessions = {}

    def addSession(self,id,startDateTime,endDateTime,name,descr,presenter):
        session = Session(id,startDateTime,endDateTime,name,descr,presenter)
        self.__sessions[id] = session
    
    def getSessions(self):
        return self.__sessions.values()
    
    def getClassName(self):
        return "Seminar"
    
    def containsSessionId(self,id):
        if id in self.__sessions:
            return True
        return False
