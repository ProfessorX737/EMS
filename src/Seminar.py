from src.Event import Event
from src.Session import Session

class Seminar(Event):
    def __init__(self,id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd):
        super().__init__(id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd)
        self.__sessions = {}

    def addSession(self,sessionId,startDateTime,endDateTime,name,descr,capacity,presenter):
        session = Session(self.getId(),sessionId,startDateTime,endDateTime,name,descr,self.getVenueName(),self.getConvener(),capacity,self.getDeregEnd(),presenter)
        self.__sessions[sessionId] = session
    
    def getSessions(self):
        return self.__sessions.values()

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
            del self.__sessions[sessionId]
    
    def isRegisteredToASession(self, userId):
        for s in self.__sessions.values():
            if s.hasAttendee(userId):
                return True
        return False
