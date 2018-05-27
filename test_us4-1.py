from src.EventManagementSystem import *
from src.Venue import *
from src.Guest import *
from src.Staff import *
from src.Seminar import *
from src.Session import *
from src.client import *
from src.exceptions.RegistrationException import *
import pytest

class TestRegisterGuestToSeminar(object):
    def setup_method(self):
        self.system = bootstrap_system()
        # add some users
        self.staffId = 1
        self.studentId = 2
        self.guestId = 3
        self.staffId2 = 4
        self.studentId2 = 5
        self.guestId2 = 6
        self.staff = self.system.addUser('Staff name',self.staffId,'staff@mail.com','pw','trainer')
        self.student = self.system.addUser("Student name",self.studentId,'student@mail.com','pw','trainee')
        self.guest = self.system.addUser('Guest name',self.guestId, 'guest@mail.com', 'pw', 'guest')
        self.staff2 = self.system.addUser('Staff2',self.staffId2,'staff2@mail.com','pw','trainer')
        self.student2 = self.system.addUser("Student2",self.studentId2,'student2@mail.com','pw','trainee')
        self.guest2 = self.system.addUser('Guest2',self.guestId2, 'guest2@mail.com', 'pw', 'guest')
        # add a self.venue
        self.venue = self.system.addVenue('venue', 'somewhere', 100)
        self.venueId = self.venue.getId()
        # create a past events
        startDateTime = create_period("2018-01-11 11:00") # past date
        endDateTime = create_period("2018-01-11 12:00")   # past date
        deregEnd = create_period("2018-01-09 09:00")      # past date
        earlybirdEnd = create_period("2018-01-07 09:00")  # past date
        self.pastSeminarId = self.system.addSeminar(self.staff,startDateTime,endDateTime,"pastSeminar","desc",self.venueId,self.staff,100,deregEnd,2,earlybirdEnd)
        self.pastCourseId = self.system.addCourse(self.staff,startDateTime,endDateTime,"pastCourse","desc",self.venueId,self.staff,100,deregEnd,2,earlybirdEnd)
        self.pastSessionId = self.system.addSession(self.staff,self.pastSeminarId,startDateTime,endDateTime,"pastSession","desc",100,self.guest)
        # create a current events
        startDateTime = create_period("2019-01-11 11:00") # future date
        endDateTime = create_period("2019-01-11 12:00")   # future date
        deregEnd = create_period("2019-01-09 09:00")      # future date
        earlybirdEnd = create_period("2019-01-07 09:00")  # future date
        self.currSeminarId = self.system.addSeminar(self.staff,startDateTime,endDateTime,"currSeminar","desc",self.venueId,self.staff,100,deregEnd,2,earlybirdEnd)
        self.currCourseId = self.system.addCourse(self.staff,startDateTime,endDateTime,"currCourse","desc",self.venueId,self.staff,100,deregEnd,2,earlybirdEnd)
        self.currSessionId = self.system.addSession(self.staff,self.currSeminarId,startDateTime,endDateTime,"currSession","desc",100,self.guest)
        # create past dereg current events
        startDateTime = create_period("2018-07-11 11:00") # future date 
        endDateTime = create_period("2018-07-11 12:00")   # future date
        deregEnd = create_period("2018-01-09 09:00")      # past date
        earlybirdEnd = create_period("2018-01-07 09:00")  # past date
        self.pastDeregCurrSeminarId = self.system.addSeminar(self.staff,startDateTime,endDateTime,"pastDeregCurrSeminarId","desc",self.venueId,self.staff,100,deregEnd,2,earlybirdEnd)
        self.pastDeregCurrCourseId = self.system.addCourse(self.staff,startDateTime,endDateTime,"pastDeregCurrCourseId","desc",self.venueId,self.staff,100,deregEnd,2,earlybirdEnd)
        self.pastDeregCurrSessionId = self.system.addSession(self.staff,self.pastDeregCurrSeminarId,startDateTime,endDateTime,"pastDeregCurrSessionId","desc",100,self.guest)
        self.pastDeregCurrSessionId2 = self.system.addSession(self.staff,self.pastDeregCurrSeminarId,startDateTime,endDateTime,"pastDeregCurrSessionId2","desc",100,self.guest)
        # create past earlybird current events
        startDateTime = create_period("2018-07-11 11:00") # future date
        endDateTime = create_period("2018-07-11 12:00")   # future date
        deregEnd = create_period("2018-07-11 09:00")      # future date
        earlybirdEnd = create_period("2018-01-07 09:00")  # past date
        self.pastEarlyBirdCurrSeminarId = self.system.addSeminar(self.staff,startDateTime,endDateTime,"pastEarlyBirdCurrSeminarId","desc",self.venueId,self.staff,100,deregEnd,2,earlybirdEnd)
        self.pastEarlyBirdCurrCourseId = self.system.addCourse(self.staff,startDateTime,endDateTime,"pastEarlyBirdCurrCourseId","desc",self.venueId,self.staff,100,deregEnd,2,earlybirdEnd)
        self.pastEarlyBirdCurrSessionId = self.system.addSession(self.staff,self.pastEarlyBirdCurrSeminarId,startDateTime,endDateTime,"pastEarlyBirdCurrSessionId","desc",100,self.guest)
        # create cancelled event
        startDateTime = create_period("2019-01-11 11:00") # future date
        endDateTime = create_period("2019-01-11 12:00")   # future date
        deregEnd = create_period("2019-01-09 09:00")      # future date
        earlybirdEnd = create_period("2019-01-07 09:00")  # future date
        self.cancelledSeminarId = self.system.addSeminar(self.staff,startDateTime,endDateTime,"cancelledSeminarId","desc",self.venueId,self.staff,100,deregEnd,2,earlybirdEnd)
        self.cancelledCourseId = self.system.addCourse(self.staff,startDateTime,endDateTime,"cancelledCourseId","desc",self.venueId,self.staff,100,deregEnd,2,earlybirdEnd)
        self.cancelledSessionId = self.system.addSession(self.staff,self.cancelledSeminarId,startDateTime,endDateTime,"cancelledSessionId","desc",100,self.guest)
        self.system.cancelEvent(self.cancelledSeminarId)
        self.system.cancelEvent(self.cancelledCourseId)
    
    def test_invalid_registration_to_closed_event_as_guest(self):
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.pastCourseId,self.guestId2)
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.pastSessionId,self.guestId2)
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.pastSeminarId,self.guestId2)

    def test_valid_reg_and_dereg_to_open_event_as_guest(self):

        course = self.system.getEvent(self.currCourseId)
        seminar = self.system.getEvent(self.currSeminarId)
        session = self.system.getEvent(self.currSessionId)

        # test that the user is registered after the registration
        self.system.registerUser(self.currCourseId,self.guestId2)
        assert self.guest2.isRegistered(self.currCourseId) == True
        self.system.registerUser(self.currSessionId,self.guestId2)
        assert self.guest2.isRegistered(self.currSessionId) == True
        self.system.registerUser(self.currSeminarId,self.guestId2)
            # testing valid registration to seminar when registered to a session
        assert self.guest2.isRegistered(self.currSeminarId) == True
        # test that the events contain the user after registration
        assert course.hasAttendee(self.guestId2) == True
        assert seminar.hasAttendee(self.guestId2) == True
        assert seminar.hasAttendee(self.guestId2) == True

        # test deregistration
        self.system.deregisterUser(self.currCourseId,self.guestId2)
        self.system.deregisterUser(self.currSeminarId,self.guestId2)
        # test that the user is no longer registered after deregistration
        assert self.guest2.isRegistered(self.currCourseId) == False
        assert self.guest2.isRegistered(self.currSeminarId) == False
        assert self.guest2.isRegistered(self.currSessionId) == False
        # test the events do not contain the user after registration
        assert course.hasAttendee(self.guestId2) == False
        assert seminar.hasAttendee(self.guestId2) == False
        assert seminar.hasAttendee(self.guestId2) == False

    def test_invalid_registration_to_cancelled_event_as_guest(self):
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.cancelledCourseId,self.guestId2)
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.cancelledSeminarId,self.guestId2)

    def test_invalid_deregistration_after_deregEnd_as_guest(self):
        
        self.system.registerUser(self.pastDeregCurrCourseId,self.guestId2)
        self.system.registerUser(self.pastDeregCurrSessionId,self.guestId2)
        self.system.registerUser(self.pastDeregCurrSeminarId,self.guestId2)
        assert self.guest2.isRegistered(self.pastDeregCurrCourseId) == True
        assert self.guest2.isRegistered(self.pastDeregCurrSessionId) == True
        assert self.guest2.isRegistered(self.pastDeregCurrSeminarId) == True

        with pytest.raises(RegistrationException):
            self.system.deregisterUser(self.pastDeregCurrCourseId,self.guestId2)
        with pytest.raises(RegistrationException):
            self.system.deregisterUser(self.pastDeregCurrSessionId,self.guestId2)
        with pytest.raises(RegistrationException):
            self.system.deregisterUser(self.pastDeregCurrSeminarId,self.guestId2)
        
    def test_invalid_registration_as_convener(self):
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.currCourseId,self.staffId)
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.currSessionId,self.staffId)
    
    def test_invalid_registration_as_speaker_guest(self):
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.currSessionId,self.guestId)

    def test_invalid_registration_to_full_event_as_guest(self):
        # create full event
        startDateTime = create_period("2019-01-11 11:00") # future date
        endDateTime = create_period("2019-01-11 12:00")   # future date
        deregEnd = create_period("2019-01-09 09:00")      # future date
        earlybirdEnd = create_period("2019-01-07 09:00")  # future date
        self.fullSeminarId = self.system.addSeminar(self.staff,startDateTime,endDateTime,"fullSeminarId","desc",self.venueId,self.staff,0,deregEnd,2,earlybirdEnd)
        self.fullCourseId = self.system.addCourse(self.staff,startDateTime,endDateTime,"fullCourseId","desc",self.venueId,self.staff,0,deregEnd,2,earlybirdEnd)
        self.fullSessionId = self.system.addSession(self.staff,self.fullSeminarId,startDateTime,endDateTime,"fullSessionId","desc",0,self.guest)

        with pytest.raises(RegistrationException):
            self.system.registerUser(self.fullSessionId,self.guestId2)
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.fullCourseId,self.guestId2)

    def test_invalid_registration_to_seminar_without_registering_to_a_session_as_guest(self):
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.currSeminarId, self.guestId2)
    
    def test_total_registration_fee_is_applied_for_guest(self):
        # test for course
        course = self.system.getEvent(self.pastEarlyBirdCurrCourseId)
        self.system.registerUser(self.pastEarlyBirdCurrCourseId, self.guestId)
        assert self.system.getCost(self.pastEarlyBirdCurrCourseId, self.guestId) == 2
        # test for seminar
        seminar = self.system.getEvent(self.currSessionId)
        self.system.registerUser(self.pastEarlyBirdCurrSessionId, self.guestId2)
        assert self.system.getCost(self.pastEarlyBirdCurrSessionId, self.guestId2) == 2

    def test_earlybird_discount_as_guest(self):
        # test for course
        course = self.system.getEvent(self.currCourseId)
        self.system.registerUser(self.currCourseId, self.guestId)
        assert self.system.getCost(self.currCourseId, self.guestId) == 1
        # test for seminar
        seminar = self.system.getEvent(self.currSessionId)
        self.system.registerUser(self.currSessionId, self.guestId2)
        assert self.system.getCost(self.currSeminarId, self.guestId2) == 1

    def test_zero_registration_fee_as_staff(self):
        # test for course
        course = self.system.getEvent(self.currCourseId)
        self.system.registerUser(self.currCourseId, self.staffId2)
        assert self.system.getCost(self.currCourseId, self.staffId2) == 0
        # test for seminar
        seminar = self.system.getEvent(self.currSessionId)
        self.system.registerUser(self.currSessionId, self.staffId2)
        assert self.system.getCost(self.currSeminarId, self.staffId2) == 0

    def test_zero_registration_fee_as_student(self):
        # test for course
        course = self.system.getEvent(self.currCourseId)
        self.system.registerUser(self.currCourseId, self.studentId2)
        assert self.system.getCost(self.currCourseId, self.studentId2) == 0
        # test for seminar
        seminar = self.system.getEvent(self.currSessionId)
        self.system.registerUser(self.currSessionId, self.studentId2)
        assert self.system.getCost(self.currSeminarId, self.studentId2) == 0

    