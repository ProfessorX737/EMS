from src.CourseManager import *
from src.SeminarManager import *
from src.StaffManager import *
from src.StudentManager import *
from src.GuestManager import *
from src.VenueManager import *
from src.Course import *
from src.Seminar import *
from src.Staff import Staff
from src.Session import Session
from src.exceptions.LoginException import *
from src.exceptions.VenueCapacityException import *
from src.exceptions.ExistingEventException import *
from src.exceptions.ExistingVenueException import *
import datetime

class EventManagementSystem():
    def __init__(self):
        self.__courseManager = CourseManager()
        self.__seminarManager = SeminarManager()
        self.__studentManager = StudentManager()
        self.__staffManager = StaffManager()
        self.__guestManager = GuestManager()
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
        user = self.__staffManager.getUserById(zid)
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

    def addCourse(self,staff,startDateTime, endDateTime, name, descr, venueName, convener, capacity, deregEnd, fee, earlybirdEnd):
        venue = self.__venueManager.getVenue(venueName)
        if (venue.getMaxCapacity() < capacity):
            raise VenueCapacityException('Capacity','Venue Capacity is less than event capacity')
        course = Course(self.getUniqueEventId(),startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd, fee, earlybirdEnd)
        if self.__courseManager.addCourse(course):
            staff.addPostedCurrEvent(course)
            return True
        else:
            raise ExistingEventException('Course', 'Course with this name already exists')

    def addSeminar(self,staff,startDateTime, endDateTime, name, descr, venueName, convener, capacity, deregEnd, fee, earlybirdEnd):
        venue = self.__venueManager.getVenue(venueName)
        if (venue.getMaxCapacity() < capacity):
            raise VenueCapacityException('Capacity','Venue Capacity is less than event capacity')
        seminar = Seminar(self.getUniqueEventId(),startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd, fee, earlybirdEnd)
        if self.__seminarManager.addSeminar(seminar):
            staff.addPostedCurrEvent(seminar)
            return True
        else:
            raise ExistingEventException('Seminar', 'Seminar with this name already exists')

    def addSession(self,seminarId, startDateTime, endDateTime, name, descr, presenter):
        seminar = self.getEvent(seminarId)
        sessionId = self.__seminarManager.addSession(seminarId,startDateTime,endDateTime,name,descr,presenter)
        self.__staffManager.notifyRegistreesNewSession(seminarId,seminar.getName(),name)
        self.__studentManager.notifyRegistreesNewSession(seminarId,seminar.getName(),name)
        self.__guestManager.notifyRegistreesNewSession(seminarId,seminar.getName(),name)
        return True

    def getSession(self,eventId,sessionId):
        self.__seminarManager.getSession(eventId,sessionId)

    def deleteEvent(self,eventId):
        self.__seminarManager.deleteEvent(eventId)
        self.__courseManager.deleteEvent(eventId)
    
    def editEvent(self,event,startDateTime,endDateTime,name,descr,venueName,convener,capacity,deregEnd):
        event.setStartDateTime(startDateTime)
        event.setEndDateTime(endDateTime)
        event.setName(name)
        event.setDescription(descr)
        event.setVenue(venueName)
        event.setConvener(convener)
        event.setCapacity(capacity)
        event.setDeregEnd(deregEnd)
        self.__staffManager.notifyRegistreesEventEdit(event.getId()) 
        self.__studentManager.notifyRegistreesEventEdit(event.getId()) 
        self.__guestManager.notifyRegistreesEventEdit(event.getId())

    def getCost(self,eventId,userId):
        if self.getUserType(userId) == "Guest":
            event = self.getEvent(eventId)
            return event.getCost()
        else:
            return 0

# ======== User Manager methods ========================================================================================
    def getStudents(self):
        return self.__studentManager.getUsers()
    def getStaff(self):
        return self.__staffManager.getUsers()
    def setStaff(self,staff):
        self.__staffManager.setUsers(staff)
    def setStudents(self,students):
        self.__studentManager.setUsers(students)
    def getCurrEvents(self,user):
        return user.getCurrEvents()
    def getPastEvents(self,user):
        return user.getPastEvents()
    def getPostedCurrEvents(self,staff):
        return self.__staffManager.getPostedCurrEvents(staff)
    def getPostedPastEvents(self,staff):
        return self.__staffManager.getPostedPastEvents(staff)
    def getCancelledEvents(self,staff):
        return self.__staffManager.getCancelledEvents(staff)
    def addUser(self,name,zID,email,password,role):
        if (role == 'trainee'):
            return self.__studentManager.addUser(name,zID,email,password,role)
        elif (role == 'trainer'):
            return self.__staffManager.addUser(name,zID,email,password,role)
        elif (role == 'guest'):
            return self.__guestManager.addUser(name,zID,email,password,role)
    def getUserById(self,zid):
        if self.__studentManager.getUserById(zid) is not None:
            return self.__studentManager.getUserById(zid)
        elif self.__staffManager.getUserById(zid) is not None:
            return self.__staffManager.getUserById(zid)
        elif self.__guestManager.getUserById(zid) is not None:
            return self.__guestManager.getUserById(zid)
        else:
            raise LoginException('User', 'Username does not exist')
    def getUserByEmail(self,email):
        if self.__studentManager.getUserByEmail(email) is not None:
            return self.__studentManager.getUserByEmail(email)
        elif self.__staffManager.getUserByEmail(email) is not None:
            return self.__staffManager.getUserByEmail(email)
        elif self.__guestManager.getUserByEmail(email) is not None:
            return self.__guestManager.getUserByEmail(email)       
    def getUserType(self,zid):
        if self.__studentManager.getUserById(zid) is not None:
            return self.__studentManager.getUserType()
        elif self.__staffManager.getUserById(zid) is not None:
            return self.__staffManager.getUserType()
        elif self.__guestManager.getUserById(zid) is not None:
            return self.__guestManager.getUserType()
    def addRegisteredEvent(self,userID,event):
        self.__staffManager.addRegisteredEvent(userID,event)
        self.__studentManager.addRegisteredEvent(userID,event)
        self.__guestManager.addRegisteredEvent(userID,event)
    def removeRegisteredEvent(self,userID,eventId):
        self.__staffManager.removeRegisteredEvent(userID,eventId)
        self.__studentManager.removeRegisteredEvent(userID,eventId)
        self.__guestManager.removeRegisteredEvent(userID,eventId)
# =========== Venue Manager methods =======================================================================================
    def addVenue(self, name, loc, capacity):
        try:
            self.__venueManager.addVenue(name, loc, capacity)
        except ExistingVenueException as errmsg:
            raise errmsg
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
        self.__studentManager.cancelEvent(convener,eventId)
        self.__staffManager.cancelEvent(convener,eventId)
        self.__guestManager.cancelEvent(convener,eventId)
        self.__courseManager.cancelEvent(eventId)
        self.__seminarManager.cancelEvent(eventId)
        convener.cancelPostedEvent(eventId)
    def checkPassword(self, user, password):
        if user.getPassword() != password:
            raise LoginException('Password','Invalid password')
        else:
            return True
# ============== private methods =========================
    def getUniqueEventId(self):
        id = 0
        while self.__courseManager.containsEventId(id) or self.__seminarManager.containsEventId(id):
            id = id + 1
        return id

    def setEvent(self,event,startDateTime,endDateTime,name,descr,venueName,convener,capacity,deregEnd,fee,earlybirdEnd):
        venue = self.__venueManager.getVenue(venueName)
        try:
            event.setStartDateTime(startDateTime)
            event.setEndDateTime(endDateTime)
            event.setName(name)
            event.setDescription(descr)
            event.setVenue(venue)
            event.setConvener(convener)
            event.setCapacity(capacity)
            event.setDeregEnd(deregEnd)
            event.setFee(fee)
            event.setEarlyBirdEnd(earlybirdEnd)       
        except VenueCapacityException as errmsg:
            raise errmsg