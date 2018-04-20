from EventManager import *
from Seminar import *
class SeminarManager(EventManager):
    def __init__(self):
        self.__events = {}
    def addSeminar(self,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd):
        seminar = Course(startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd)
        self.__events[seminar.getName()] = seminar
    def addSession(seminarName, startDateTime, endDateTime, name, descr, presenter):
        session = Session(startDateTime, endDateTime, name, descr, presenter)
        self.__events[seminarName].addSession(session)
    def getSession(seminarName,sessionName):
        seminar = self.__events[seminarName]
        session = seminar.getSession(sessionName)