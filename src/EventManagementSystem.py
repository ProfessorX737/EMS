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
from src.exceptions.UserExistsException import *
from src.exceptions.RegistrationException import *
from src.exceptions.SessionDateTimeException import *
from src.exceptions.OverlappingBookingException import *
from src.exceptions.InvalidEventDateException import *
from src.Notification import *
from src.Period import *
import datetime

class EventManagementSystem():
    def __init__(self):
        self.__courseManager = CourseManager()
        self.__seminarManager = SeminarManager()
        self.__studentManager = StudentManager()
        self.__staffManager = StaffManager()
        self.__guestManager = GuestManager()
        self.__venueManager = VenueManager()

    def getStudentManager(self):
        return self.__studentManager
    def getStaffManager(self):
        return self.__staffManager
    def getGuestManager(self):
        return self.__guestManager
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
    def registerUserToSession(self,eventId,user):
        self.__seminarManager.registerUserToSession(eventId,user)
    def deregisterUserFromSeminar(self,eventId,userID):
        self.__seminarManager.deregisterUser(eventId,userID)
    def deregisterUserFromCourse(self,eventId,userID):
        self.__courseManager.deregisterUser(eventId,userID)
    def deregisterUserFromSession(self,eventId,userID):
        self.__seminarManager.deregisterUserFromSession(eventId,userID)

    def registerUser(self,eventId,userId):
        event = self.getEvent(eventId)
        user = self.getUserById(userId)
        if event.isCancelled():
            raise RegistrationException("cancelled","Cannot register to a cancelled event")
        if not event.isOpen():
            raise RegistrationException("endDateTime", "Cannot register to a closed event")
        if event.getConvenerId() == userId:
            raise RegistrationException("convener","The convener of an event cannot register to their own event")
        if event.isFull():
            raise RegistrationException("capacity","Cannot register to a full event")

        if isinstance(event,Course):
            self.registerUserToCourse(eventId,user)
            self.addRegisteredEvent(userId,event)
        if isinstance(event,Seminar):
            if not event.isRegisteredToASession(userId):
                raise RegistrationException("session","To register you must be registered to at least one session")
            self.registerUserToSeminar(eventId,user)
            self.addRegisteredEvent(userId,event)
        if isinstance(event,Session):
            if event.getPresenterId() == userId:
                raise RegistrationException("presenter","The presenter of a session cannot register to their own session")
            self.registerUserToSession(eventId,user)
            self.registerUserToSeminar(event.getSeminarId(),user)
            seminar = self.getEvent(event.getSeminarId())
            self.addRegisteredEvent(userId,seminar)
            self.addRegisteredEvent(userId,event)

    def deregisterUser(self,eventId,userId):
        event = self.getEvent(eventId)
        if event.isPastDeregEnd():
            raise RegistrationException("deregEnd","Cannot deregister after deregistration period")
        self.removeRegisteredEvent(userId,eventId)
        if isinstance(event,Course):
            self.deregisterUserFromCourse(eventId,userId)
        if isinstance(event,Seminar):
            self.deregisterUserFromSeminar(eventId,userId)
            for session in event.getSessions():
                self.deregisterUserFromSession(session.getId(),userId)
                self.removeRegisteredEvent(userId,session.getId())
        if isinstance(event,Session):
            self.deregisterUserFromSession(eventId,userId)
            seminar = self.getEvent(event.getSeminarId())
            if not seminar.isRegisteredToASession(userId):
                self.deregisterUserFromSeminar(event.getSeminarId(),userId)
                self.removeRegisteredEvent(userId,event.getSeminarId())

    # returns true if the user is the convener of the event
    def isMyEvent(self,userId,eventId):
        try:
            user = self.getUserById(userId)
        except LoginException:
            return False
        else:
            if user.isMyEvent(eventId):
                return True
        return False
    # returns true if the user is the presenter of the session or a presenter at the seminar
    def isPresenterAtEvent(self,userId,eventId):
        try:
            user = self.getUserById(userId)
        except LoginException:
            return False
        else:
            event = self.getEvent(eventId)
            if event is None:
                return False
            if isinstance(event,Session):
                if event.getPresenterId() == userId:
                    return True
            if isinstance(event,Seminar):
                return event.isPresenterOfASession(userId)
        return False

    def getEvent(self,eventId):
        event = self.__courseManager.getEvent(eventId)
        if event is None:
            event = self.__seminarManager.getEvent(eventId)
        if event is None:
            event = self.getSession(eventId)
        return event
    def getSessions(self,eventId):
        return self.__seminarManager.getSessions(eventId)

    def getSession(self,sessionId):
        return self.__seminarManager.getSession(sessionId)

    # adds a course to the course manager, returns the id generated for the new course
    def addCourse(self,staff,startDateTime, endDateTime, name, descr, venueId, convener, capacity, deregEnd, fee, earlybirdEnd):
        venue = self.__venueManager.getVenue(venueId)
        if (venue.getMaxCapacity() < capacity):
            raise VenueCapacityException('Capacity','Venue Capacity is less than event capacity')
        id = self.getUniqueEventId()
        course = Course(id,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd, fee, earlybirdEnd)
        try:
            if venue.overlaps(course.getPeriod()):
                raise OverlappingBookingException('Event', 'Overlapping booking time with previously booked event at this venue')
            if self.__courseManager.addCourse(course):
                venue.addPeriod(course.getPeriod())
                staff.addPostedCurrEvent(course)
            else:
                raise ExistingEventException('Course', 'Course with this name already exists')
            return id
        except InvalidEventDateException as errMsg:
            raise errMsg

    # adds a seminar to the seminar manager, returns the id generated for the new seminar
    def addSeminar(self,staff,startDateTime, endDateTime, name, descr, venueId, convener, capacity, deregEnd, fee, earlybirdEnd):
        venue = self.__venueManager.getVenue(venueId)
        if (venue.getMaxCapacity() < capacity):
            raise VenueCapacityException('Capacity','Venue Capacity is less than event capacity')
        id = self.getUniqueEventId()
        seminar = Seminar(id,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd, fee, earlybirdEnd)
        try:
            if venue.overlaps(seminar.getPeriod()):
                raise OverlappingBookingException('Event', 'Overlapping booking time with previously booked event at this venue')  
            if self.__seminarManager.addSeminar(seminar):
                venue.addPeriod(seminar.getPeriod())
                staff.addPostedCurrEvent(seminar)
            else:
                raise ExistingEventException('Seminar', 'Seminar with this name already exists')
            return id
        except InvalidEventDateException as errMsg:
            raise errMsg

    # adds a session to a seminar in the seminar manager, returns the id generated for the session which is unique among\
    # courses and seminars
    def addSession(self,staff,seminarId,startDateTime,endDateTime,name,descr,capacity,presenter):
        seminar = self.getEvent(seminarId)
        venue = seminar.getVenue()
        if (venue.getMaxCapacity() < capacity):
            raise VenueCapacityException('Capacity','Venue Capacity is less than session capacity')
        if (startDateTime < seminar.getStartDateTime()):
            raise SessionDateTimeException('StartDateTime', 'Session start date time > seminar start date time')
        if (endDateTime > seminar.getEndDateTime()):
            raise SessionDateTimeException('EndDateTime', 'Session end date time <= seminar end date time')
        id = self.getUniqueEventId()
        session = Session(seminarId,id,startDateTime,endDateTime,name,descr,seminar.getVenue(),\
        seminar.getConvener(),capacity,seminar.getDeregEnd(),presenter,seminar.getFee(),seminar.getEarlyBirdEnd())
        if seminar.sessionPeriodOverlaps(session.getPeriod()):
            raise OverlappingBookingException('Session', 'Session time overlaps with previous booking at this venue') 
        if not self.__seminarManager.addSession(seminarId,session):
            raise ExistingEventException('Session', 'Session in this seminar, with this name already exists')
        staff.addPostedCurrEvent(session)
        # if you are making the session and set the presenter to be yourself then you automatically accept the request
        if staff.get_id() != presenter.get_id():
            guestRequestNotification = AcceptRejectNotification("{0} has asked you to be the presenter to '{1}' session".format(staff.getName(),name),session.getId())
            presenter.addNotification(guestRequestNotification)
        else:
            session.setIsPending(False)
        return id

    def deleteEvent(self,eventId):
        self.__seminarManager.deleteEvent(eventId)
        self.__courseManager.deleteEvent(eventId)

    def setEvent(self,event,startDateTime,endDateTime,name,descr,venueName,capacity,deregEnd,fee,earlybirdEnd):
        oldEventName = event.getName()
        venue = self.__venueManager.getVenue(venueName)
        if isinstance(event,Course):
            if self.__courseManager.containsEventName(event.getId(),name):
                raise ExistingEventException('Name','Event with this name already exists')
        elif isinstance(event,Seminar):
            if self.__seminarManager.containsEventName(event.getId(),name):
                raise ExistingEventException('Name','Event with this name already exists')
        try:
            event.setStartDateTime(startDateTime)
            event.setEndDateTime(endDateTime)
            event.setName(name)
            event.setDescription(descr)
            event.setVenue(venue)
            event.setCapacity(capacity)
            event.setDeregEnd(deregEnd)
            event.setFee(fee)
            event.setEarlyBirdEnd(earlybirdEnd)       
        except VenueCapacityException as errmsg:
            raise errmsg
        except OverlappingBookingException as errmsg:
            raise errmsg
        except InvalidEventDateException as errmsg:
            raise errmsg
        if(oldEventName != name):
            changedNameNotification = DeletableNotification("'{0}' event was renamed '{1}'".format(oldEventName,name))
            self.notifyRegistrees(event.getId(),changedNameNotification)
        eventEditedNotification = DeletableNotification("The event details of '{0}' were edited".format(name))
        self.notifyRegistrees(event.getId(),eventEditedNotification)

    def notifyRegistrees(self,eventId,notification):
        self.__staffManager.notifyRegistrees(eventId,notification) 
        self.__studentManager.notifyRegistrees(eventId,notification) 
        self.__guestManager.notifyRegistrees(eventId,notification) 
    
    def editSession(self,session,startDateTime,endDateTime,name,descr,presenter,capacity):
        seminar = self.getEvent(session.getSeminarId())
        venue = seminar.getVenue()
        if (venue.getMaxCapacity() < capacity):
            raise VenueCapacityException('Capacity','Venue Capacity is less than session capacity')
        if (startDateTime < seminar.getStartDateTime()):
            raise SessionDateTimeException('StartDateTime', 'Session start date time must be >= seminar start date time')
        if (endDateTime > seminar.getEndDateTime()):
            raise SessionDateTimeException('EndDateTime', 'Session end date time must be <= seminar end date time')
        oldStartDateTime = session.getStartDateTime()
        oldEndDateTime = session.getEndDateTime()
        session.setStartDateTime(startDateTime)
        session.setEndDateTime(endDateTime)
        if seminar.sessionPeriodOverlaps(session.getPeriod()):
            session.setStartDateTime(oldStartDateTime)
            session.setEndDateTime(oldEndDateTime)
            raise OverlappingBookingException('Session', 'Session time overlaps with previous booking at this venue') 

        if session.getName() != name:
            changedNameNotification = DeletableNotification("'{0}' session was renamed '{1}'".format(session.getName(),name))
            self.notifyRegistrees(session.getId(),changedNameNotification)
        sessionEditedNotification = DeletableNotification("The session details of '{0}' were edited".format(name))
        self.notifyRegistrees(session.getId(),sessionEditedNotification)
        # if the new presenter does not equal to the old presenter
        if presenter.get_id() != session.getPresenterId():
            # if the old presenter is you, you do not need to be notified because you are editing the session
            if session.getConvenerId() != session.getPresenterId():
                # if the session is still pending, the presenter has not yet accepted the request so tailor the message
                if(session.getIsPending() == False):
                    changedPresenterNotification = DeletableNotification("You are no longer the presenter of '{0}' session".format(session.getName()))
                else:
                    changedPresenterNotification = DeletableNotification("You are not asked to be the presenter for '{0}' session anymore".format(session.getName()))
                session.notifyPresenter(changedPresenterNotification)
            # if you changed the presenter to be yourself, then you also don't need to be notified
            if session.getConvenerId() != presenter.get_id():
                guestRequestNotification = AcceptRejectNotification("{0} has asked you to be the presenter to '{1}' session".format(session.getConvenerName(),name),session.getId())
                presenter.addNotification(guestRequestNotification)
                session.setIsPending(True)
        # session.setStartDateTime(startDateTime)
        # session.setEndDateTime(endDateTime)
        session.setName(name)
        session.setDescription(descr)
        session.setPresenter(presenter)
        session.setCapacity(capacity)

    def getCost(self,eventId,userId):
        user = self.getUserById(userId)
        if self.getUserType(userId) == "Guest":
            if self.__seminarManager.isSessionPresenter(eventId,userId) is True:
                return 0
            else:
                event = self.getEvent(eventId)
                return event.getCost()
        else:
            return 0

# ======== User Manager methods ========================================================================================
    def getStudents(self):
        return self.__studentManager.getUsers()
    def getStaff(self):
        return self.__staffManager.getUsers()
    def getGuests(self):
        return self.__guestManager.getUsers()
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
        try:
            if (role == 'trainee'):
                return self.__studentManager.addUser(name,zID,email,password,role)
            elif (role == 'trainer'):
                return self.__staffManager.addUser(name,zID,email,password,role)
            elif (role == 'guest'):
                return self.__guestManager.addUser(name,zID,email,password,role)
        except UserExistsException as errMsg:
            raise errMsg
    def getUserById(self,zid):
        if self.__studentManager.getUserById(zid) is not None:
            return self.__studentManager.getUserById(zid)
        elif self.__staffManager.getUserById(zid) is not None:
            return self.__staffManager.getUserById(zid)
        elif self.__guestManager.getUserById(zid) is not None:
            return self.__guestManager.getUserById(zid)
        else:
            raise LoginException('User', 'Username does not exist')
    def userIdExists(self,userId):
        if self.__studentManager.getUserById(userId) is not None or\
        self.__studentManager.getUserById(userId) is not None or\
        self.__guestManager.getUserById(userId) is not None:
            return True
        return False
    def getUser(self, identifier):
        try:
            user = self.getUserById(identifier)
            return user
        except LoginException as errMsg:
            try:
                user = self.getUserByEmail(identifier)
                return user
            except LoginException as errMsg:
                raise errMsg    
    def getUserByEmail(self,email):
        if self.__studentManager.getUserByEmail(email) is not None:
            return self.__studentManager.getUserByEmail(email)
        elif self.__staffManager.getUserByEmail(email) is not None:
            return self.__staffManager.getUserByEmail(email)
        elif self.__guestManager.getUserByEmail(email) is not None:
            return self.__guestManager.getUserByEmail(email)
        else:
            raise LoginException('User','Username does not exist')       
    def userEmailExists(self,userId):
        if self.__studentManager.getUserByEmail(userId) is not None or\
        self.__studentManager.getUserByEmail(userId) is not None or\
        self.__guestManager.getUserByEmail(userId) is not None:
            return True
        return False
    def getUserType(self,userId):
        if self.__studentManager.getUserById(userId) is not None:
            return self.__studentManager.getUserType()
        elif self.__staffManager.getUserById(userId) is not None:
            return self.__staffManager.getUserType()
        elif self.__guestManager.getUserById(userId) is not None:
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
            venueId = self.__venueManager.getIdByName(name)
            return self.__venueManager.addVenue(venueId, name,loc, capacity)
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
    def cancelEvent(self,eventId):
        event = self.getEvent(eventId)
        self.__studentManager.cancelEvent(eventId)
        self.__staffManager.cancelEvent(eventId)
        self.__guestManager.cancelEvent(eventId)
        self.__courseManager.cancelEvent(eventId)
        self.__seminarManager.cancelEvent(eventId)
        if isinstance(event,Seminar):
            for session in event.getSessions():
                presenter = session.getPresenter()
                deletedSeminarNotification = DeletableNotification("'{0}' seminar was cancelled".format(event.getName()))
                presenter.addNotification(deletedSeminarNotification)
                presenter.deleteSession(session.getId())
        convener = event.getConvener()
        if isinstance(event,Session):
            convener.deletePostedEvent(eventId)
        else:
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
    def getUniquePeriodIdForVenue(self, venueId):
        id = 0
        while self.__venueManager.venueContainsPeriodId(venueId,id):
            id = id + 1
        return id