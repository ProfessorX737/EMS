from src.CourseManager import *
from src.SeminarManager import *
from src.UserManager import *
from src.VenueManager import *
from src.Course import *
from src.Seminar import *
from src.Staff import Staff
from src.Session import Session
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
    def registerUserToSeminar(self,eventId,user):
        self.__seminarManager.registerUser(eventId,user)
    def registerUserToCourse(self,eventId,user):
        self.__courseManager.registerUser(eventId,user)
    def deregisterUserFromSeminar(self,eventId,userID):
        self.__seminarManager.deregisterUser(eventId,userID)
    def deregisterUserFromCourse(self,eventId,userID):
        self.__courseManager.deregisterUser(eventId,userID)
    def isMyEvent(self,zid,eventId):
        user = self.__userManager.getUser(zid)
        if not isinstance(user,Staff):
            return False
        for e in self.getPostedCurrEvents(user):
            if eventId == e.getId():
                return True
        return False
    def getEvent(self,eventId):
        event = self.__courseManager.getEvent(eventId)
        if event is None:
            event = self.__seminarManager.getEvent(eventId)
        return event
    def getSessions(self,eventId):
        return self.__seminarManager.getSessions(eventId)

    def addCourse(self,staff,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd, fee, earlybirdEnd):
        course = Course(self.getUniqueEventId(),startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd, fee, earlybirdEnd)
        if self.__courseManager.addCourse(course):
            staff.addPostedCurrEvent(course)
            return True
        return False

    def addSeminar(self,staff,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd, fee, earlybirdEnd):
        seminar = Seminar(self.getUniqueEventId(),startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd, fee, earlybirdEnd)
        if self.__seminarManager.addSeminar(seminar):
            staff.addPostedCurrEvent(seminar)
            return True
        return False

    def addSession(self,seminarId, startDateTime, endDateTime, name, descr, presenter):
        seminar = self.getEvent(seminarId)
        sessionId = self.__seminarManager.addSession(seminarId,startDateTime,endDateTime,name,descr,presenter)
        self.__userManager.notifyRegistreesNewSession(seminarId,seminar.getName(),name)
        return True

    def getSession(self,eventId,sessionId):
        self.__seminarManager.getSession(eventId,sessionId)

    def deleteEvent(self,eventId):
        self.__seminarManager.deleteEvent(eventId)
        self.__courseManager.deleteEvent(eventId)

    def getCost(self,eventId,userId):
        if self.getUserType(userId) is None:
            event = self.getEvent(self,eventId)
            return event.getCost()
        else:
            return 0

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
    def removeRegisteredEvent(self,userID,eventId):
        self.__userManager.removeRegisteredEvent(userID,eventId)
    # def changeRegisteredEvent(self,oldEventName,attendees,editedEvent):
    #     editedEvent.setAttendees(attendees)
    #     self.__userManager.changeRegisteredEvent(oldEventName,editedEvent)
# =========== Venue Manager methods =======================================================================================
    def addVenue(self, name, loc, capacity):
        self.__venueManager.addVenue(name, loc, capacity)
    def removeVenue(self, venueId):
        self.__venueManager.removeVenue(venueId)
    def getVenues(self):
        return self.__venueManager.getVenues()
    def getFreeTimes(self, venueId):
        return self.__venueManager.getFreeTimes(venueId)
    def getVenueNames(self):
        return self.__venueManager.getVenueNames()
# ============ mixed methods ===============================================================================================
    def cancelEvent(self,convener,eventId):
        event = self.getEvent(eventId)
        self.__userManager.cancelEvent(convener,eventId)
        self.__courseManager.cancelEvent(eventId)
        self.__seminarManager.cancelEvent(eventId)
# ============== private methods =========================
    def getUniqueEventId(self):
        id = 0
        while self.__courseManager.containsEventId(id) or self.__seminarManager.containsEventId(id):
            id = id + 1
        return id


    # def parseDateTime(self,dateTimeString):
    #     return datetime.datetime.strptime(dateTimeString,"%d-%m-%Y %H:%M")