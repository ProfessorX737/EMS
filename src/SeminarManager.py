from src.EventManager import *
from src.Seminar import *
from src.Session import Session
class SeminarManager(EventManager):
    def __init__(self):
        super().__init__()
    def addSeminar(self,seminar):
        self.addEvent(seminar)

    def addSession(self,seminarName,session):
        seminar = self.getEvent(seminarName)
        seminar.addSession(session)

    def getSession(self,seminarName,sessionName):
        seminar = self.__events[seminarName]
        session = seminar.getSession(sessionName)
        return session
    
    def getSessions(self,seminarName):
        seminar = self.getEvent(seminarName)
        return seminar.getSessions()