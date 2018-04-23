from EventManager import *
from Seminar import *
from Session import Session
class SeminarManager(EventManager):
    def __init__(self):
        super().__init__()
    def addSeminar(self,seminar):
        self.addEvent(seminar)


        
    def addSession(self,seminarName, startDateTime, endDateTime, name, descr, presenter):
        session = Session(seminarName,startDateTime, endDateTime, name, descr, presenter)
        seminar = self.getEvent(seminarName)
        seminar.addSession(session)

    def getSession(self,seminarName,sessionName):
        seminar = self.__events[seminarName]
        session = seminar.getSession(sessionName)
        return session