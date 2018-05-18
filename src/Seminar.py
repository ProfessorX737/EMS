from src.Event import Event
from src.Session import Session

class Seminar(Event):
    def __init__(self,id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,fee,earlybirdEnd):
        super().__init__(id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,fee,earlybirdEnd)
        self.__sessions = {}

    def addSession(self,session):
        self.__sessions.append(session)
        print("ADDED SESSION", session.getName())

    def getSessions(self):
        return self.__sessions

    def getClassName(self):
        return "Seminar"

    def containsSessionId(self,id):
        if id in self.__sessions:
            return True
        return False
