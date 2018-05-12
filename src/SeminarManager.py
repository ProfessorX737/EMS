from src.EventManager import *
from src.Seminar import *
from src.Session import Session
class SeminarManager(EventManager):
    def __init__(self):
        super().__init__()
    def addSeminar(self,seminar):
        return self.addEvent(seminar)

    # return session id
    def addSession(self,seminarId,startDateTime,endDateTime,name,descr,presenter):
        seminar = self.getEvent(seminarId)
        return seminar.addSession(self.__getUniqueSessionId(),startDateTime,endDateTime,name,descr,presenter)

    def getSession(self,seminarId,sessionId):
        seminar = self.__events[seminarId]
        session = seminar.getSession(sessionId)
        return session
    
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