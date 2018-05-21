from src.Event import Event
from src.Session import Session

class Seminar(Event):
    def __init__(self,id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,fee,earlybirdEnd):
        super().__init__(id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,fee,earlybirdEnd)
        self.__sessions = {}

    def addSession(self,session):
        self.__sessions[session.getId()] = session
    
    def getSessions(self):
        return self.__sessions.values()

    def getSessionIds(self):
        return self.__sessions

    def getSession(self,sessionId):
        return self.__sessions.get(sessionId)
    
    def getClassName(self):
        return "Seminar"

    def containsSessionId(self,id):
        if id in self.__sessions:
            return True
        return False

    def deleteSession(self, sessionId):
        if sessionId in self.__sessions:
            self.cancelPeriod(sessionId)
            del self.__sessions[sessionId]
            return True
        return False

    def isRegisteredToASession(self, userId):
        for s in self.__sessions.values():
            if s.hasAttendee(userId):
                return True
        return False
    
    def isPresenterOfASession(self,userId):
        for s in self.__sessions.values():
            if s.getPresenterId() == userId:
                return True
        return False
