from src.Event import Event
from src.Session import Session

class Seminar(Event):
    def __init__(self,id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd):
        super().__init__(id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd)
        self.__sessions = {}

    def addSession(self,session):
        t = (i.getStartDateTime() < session.getStartDateTime()
            and session.getStartDateTime() < i.getStartDateTime
            for i in self.__sessions)
        if any(t):
            self.__sessions.append(session)
            print("ADDED SESSION", session.getName())
        print("INVALID PERIOD")

    def getSessions(self):
        return self.__sessions

    def getClassName(self):
        return "Seminar"

    def containsSessionId(self,id):
        if id in self.__sessions:
            return True
        return False
