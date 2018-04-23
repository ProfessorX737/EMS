from CourseManager import *
from SeminarManager import *
from UserManager import *
from VenueManager import *
import datetime

class EventManagementSystem():
    def __init__(self):
        self.__courseManager = CourseManager()
        self.__seminarManager = SeminarManager()
        self.__userManager = UserManager()
        self.__venueManager = VenueManager()

    # Get events from both managers. 
    def getEvents(self):
        events = []
        for e in self.__courseManager.getEvents():
            events.append(e)
        for e in self.__seminarManager.getEvents():
            events.append(e)
        return events
    def getCurrentSeminars(self):
        return self.__seminarManager.getCurrentEvents()
    def getPastSeminars(self):
        return self.__seminarManager.getPastEvents()
    def getCurrentCourses(self):
        return self.__courseManager.getCurrentEvents()
    def getPastCourses(self):
        return self.__courseManager.getPastEvents()

    def getEvent(self,eventName):
        event = self.__courseManager.getEvent(eventName)
        if event is None:
            event = self.__courseManager.getEvent(eventName)
        return event

    def addCourse(self,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd):
        self.__courseManager.addCourse(startDateTime,endDateTime, name, descr, venue, convener, capacity,deregEnd)

    def addSeminar(self,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd):
        self.__seminarManager.addSeminar(startDateTime,endDateTime, name, descr, venue, convener, capacity,deregEnd)
    def getSession(self,seminarName,sessionName):
        self.__seminarManager.getSession(seminarName,sessionName)

    def getStudents(self):
        return self.__userManager.getStudents()
    def getStaff(self):
        return self.__userManager.getStaff()
    def setStaff(self,staff):
        self.__userManager.setStaff(staff)
    def setStudents(self,students):
        self.__userManager.setStudents(students)
    def getCurrEvents(self,user):
        return self.__userManager.getCurrEvents(user)
    def getPastEvents(self,user):
        return self.__userManager.getPastEvents(user)
    def getPostedCurrEvents(self,staff):
        return self.__userManager.getPostedCurrEvents(staff)
    def getPostedPastEvents(self,staff):
        return self.__userManager.getPostedPastEvents(staff)
    def getCancelledEvents(self,staff):
        return self.__userManager.getCancelledEvents(staff)
    def addUser(self,name,zID,email,password,role):
        self.__userManager.addUser(name,zID,email,password,role)
    def getUser(self,zid):
        return self.__userManager.getUser(zid)
    def getUserType(self,zid):
        return self.__userManager.getUserType(zid)

    def addVenue(self, name, loc):
        self.__venueManager.addVenue(name, loc)

    def removeVenue(self, name):
        self.__venueManager.removeVenue(name)

    def getVenues(self):
        self.__venueManager.getVenues()

    def getFreeTimes(self, name):
        self.__venueManager.getFreeTimes(name)

    # def parseDateTime(self,dateTimeString):
    #     return datetime.datetime.strptime(dateTimeString,"%d-%m-%Y %H:%M")