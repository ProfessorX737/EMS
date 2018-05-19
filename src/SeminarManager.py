from src.EventManager import *
from src.Seminar import *
from src.Session import Session
class SeminarManager(EventManager):
    def __init__(self):
        super().__init__()
    def addSeminar(self,seminar):
        return self.addEvent(seminar)

    def addSession(self,seminarId,session):
        seminar = self.getEvent(seminarId)
        seminar.addSession(session)
    
    def getSession(self,sessionId):
        for seminar in super().getEvents():
            if seminar.containsSessionId(sessionId):
                return seminar.getSession(sessionId)
        return None
    
    def getSessions(self,seminarId):
        seminar = self.getEvent(seminarId)
        return seminar.getSessions()
    
    def __getUniqueSessionId(self):
        id = 0
        while self.__sessionIdExists(id):
            id = id + 1
        return id
    
    def __sessionIdExists(self, id):
        for seminar in super().getEvents():
            if seminar.containsSessionId(id):
                return True 
        return False

    def containsEventId(self,id):
        if super().containsEventId(id) or self.__sessionIdExists(id):
            return True
        return False

    def cancelEvent(self,eventId):
        if super().cancelEvent(eventId) == True:
            return True
        for seminar in super().getEvents():
            seminar.deleteSession(eventId)
            return True
        return False
    
    def registerUserToSession(self,sessionId,user):
        session = self.getSession(sessionId)
        if session is None:
            return False
        session.addAttendee(user)
        return True
    
    def deregisterUserFromSession(self,sessionId,userID):
        session = self.getSession(sessionId)
        if session is None:
            return False
        session.removeAttendee(userID)