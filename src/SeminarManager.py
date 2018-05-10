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

    def getSession(self,seminarId,sessionId):
        seminar = self.__events[seminarId]
        session = seminar.getSession(sessionId)
        return session
    
    def getSessions(self,seminarId):
        seminar = self.getEvent(seminarId)
        return seminar.getSessions()