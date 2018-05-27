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

    def getNumSessions(self):
        return len(self.__sessions.values())
    
    def getClassName(self):
        return "Seminar"

    def containsSessionId(self,id):
        if id in self.__sessions:
            return True
        return False
    
    def getCapacity(self):
        capacity = 0
        for session in self.__sessions.values():
            capacity = capacity + session.getCapacity()
        return capacity

    def cancelPeriod(self,eventId):
        venue = self.getVenue()
        venue.deletePeriod(eventId)

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

    def sessionPeriodOverlaps(self,period):
        for s in self.getSessions():
            if s.getStartDateTime() <= period.getEndDateTime() \
                and s.getEndDateTime() >= period.getStartDateTime():
                return True
        return False