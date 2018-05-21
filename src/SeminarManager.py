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
        if not self.containsSessionName(seminarId, session.getName()):
            seminar.addSession(session)
            return True
        return False
    
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
            if seminar.deleteSession(eventId):
                return True
        return False
    
    def registerUserToSession(self,sessionId,user):
        session = self.getSession(sessionId)
        if session is None:
            return False
        session.addAttendee(user)
        return True
    
    def deregisterUserFromSession(self,sessionId,userId):
        session = self.getSession(sessionId)
        if session is None:
            return False
        session.removeAttendee(userId)

    def isSessionPresenter(self,seminarId,userId):
        seminar = self.getEvent(seminarId)
        if seminar is None:
            return False
        for session in seminar.getSessions():
            if session.getPresenterId() == userId:
                return True
        return False

    def containsSessionName(self,seminarId,sessionName):
        seminar = self.getEvent(seminarId)
        for s in seminar.getSessions():
            if s.getName() == sessionName:
                return True
        return False