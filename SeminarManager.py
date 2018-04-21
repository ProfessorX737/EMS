from EventManager import *
from Seminar import *
class SeminarManager(EventManager):
    def __init__(self):
        super().__init__()
    def addSeminar(self,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd):
        seminar = Seminar(startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd)
        self.__events[seminar.getName()] = seminar
    def addSession(self,seminarName, startDateTime, endDateTime, name, descr, presenter):
        session = Session(startDateTime, endDateTime, name, descr, presenter)
        self.__events[seminarName].addSession(session)
    def getSession(self,seminarName,sessionName):
        seminar = self.__events[seminarName]
        session = seminar.getSession(sessionName)
        return session