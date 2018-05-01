from CourseManager import *
from SeminarManager import *
from UserManager import *
from VenueManager import *
from Course import *
from Seminar import *
from Staff import Staff
from Session import Session
import datetime

class EventManagementSystem():
    def __init__(self):
        self.__courseManager = CourseManager()
        self.__seminarManager = SeminarManager()
        self.__userManager = UserManager()
        self.__venueManager = VenueManager()

# ========== EventManager Methods ====================================================================
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
    def registerUserToSeminar(self,seminarName,user):
        self.__seminarManager.registerUser(seminarName,user)
    def registerUserToCourse(self,courseName,user):
        self.__courseManager.registerUser(courseName,user)
    def deregisterUserFromSeminar(self,seminarName,userID):
        self.__seminarManager.deregisterUser(seminarName,userID)
    def deregisterUserFromCourse(self,courseName,userID):
        self.__courseManager.deregisterUser(courseName,userID)
    def isMyEvent(self,zid,eventName):
        user = self.__userManager.getUser(zid)
        if not isinstance(user,Staff):
            return False
        for e in self.getPostedCurrEvents(user):
            if eventName == e.getName():
                return True
        return False

    def getEvent(self,eventName):
        event = self.__courseManager.getEvent(eventName)
        if event is None:
            event = self.__seminarManager.getEvent(eventName)
        return event
    def getSessions(self,seminarName):
        return self.__seminarManager.getSessions(seminarName)

    def addCourse(self,staff,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd):
        course = Course(startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd)
        self.__courseManager.addCourse(course)
        print("Course name is ", course.getName())
        staff.addPostedCurrEvent(course)

    def addSeminar(self,staff,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd):
        seminar = Seminar(startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd)
        self.__seminarManager.addSeminar(seminar)
        staff.addPostedCurrEvent(seminar)
    def addSession(self,seminarName, startDateTime, endDateTime, name, descr, presenter):
        session = Session(seminarName, startDateTime, endDateTime, name, descr, presenter)
        self.__seminarManager.addSession(seminarName,session)

    def getSession(self,seminarName,sessionName):
        self.__seminarManager.getSession(seminarName,sessionName)

    def deleteEvent(self,event):
        if isinstance(event,Seminar):
            self.__seminarManager.deleteEvent(event)
        else:
            self.__courseManager.deleteEvent(event)

# ======== User Manager methods ========================================================================================
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
    def addRegisteredEvent(self,userID,event):
        self.__userManager.addRegisteredEvent(userID,event)
    def removeRegisteredEvent(self,userID,eventName):
        self.__userManager.removeRegisteredEvent(userID,eventName)
# =========== Venue Manager methods =======================================================================================
    def addVenue(self, name, loc):
        self.__venueManager.addVenue(name, loc)
    def removeVenue(self, name):
        self.__venueManager.removeVenue(name)
    def getVenues(self):
        self.__venueManager.getVenues()
    def getFreeTimes(self, name):
        self.__venueManager.getFreeTimes(name)
# ============ mixed methods ===============================================================================================
    def cancelEvent(self,convener,eventName):
        event = self.getEvent(eventName)
        self.__userManager.cancelEvent(convener,eventName)
        self.__courseManager.cancelEvent(eventName)
        self.__seminarManager.cancelEvent(eventName)
    


    # def parseDateTime(self,dateTimeString):
    #     return datetime.datetime.strptime(dateTimeString,"%d-%m-%Y %H:%M")