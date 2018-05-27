from src.EventManagementSystem import *
from src.GuestManager import *
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
        self.venue1 = self.system.addVenue('1', '1', 100)
        self.venueId1 = self.venue1.getId()
        self.venue2 = self.system.addVenue('2', '2', 100)
        self.venueId2 = self.venue2.getId()
        self.venue3 = self.system.addVenue('3', '3', 100)
        self.venueId3 = self.venue3.getId()
        self.venue4 = self.system.addVenue('4', '4', 100)
        self.venueId4 = self.venue4.getId()
        self.venue5 = self.system.addVenue('5', '5', 100)
        self.venueId5 = self.venue5.getId()
        self.venue6 = self.system.addVenue('6', '6', 100)
        self.venueId6 = self.venue6.getId()
        self.venue7 = self.system.addVenue('7', '7', 100)
        self.venueId7 = self.venue7.getId()
        self.venue8 = self.system.addVenue('8', '8', 100)
        self.venueId8 = self.venue8.getId()
        self.venue9 = self.system.addVenue('9', '9', 100)
        self.venueId9 = self.venue9.getId()
        self.venue10 = self.system.addVenue('10', '10', 100)
        self.venueId10 = self.venue10.getId()
        # create a current events
        startDateTime = create_period("2019-01-11 11:00") # future date
        endDateTime = create_period("2019-01-11 12:00")   # future date
        deregEnd = create_period("2019-01-09 09:00")      # future date
        earlybirdEnd = create_period("2019-01-07 09:00")  # future date
        self.currSeminarId = self.system.addSeminar(self.staff,startDateTime,endDateTime,"currSeminar","desc",self.venueId1,self.staff,100,deregEnd,2,earlybirdEnd)
        self.currCourseId = self.system.addCourse(self.staff,startDateTime,endDateTime,"currCourse","desc",self.venueId2,self.staff,100,deregEnd,2,earlybirdEnd)
        self.currSessionId = self.system.addSession(self.staff,self.currSeminarId,startDateTime,endDateTime,"currSession","desc",100,self.guest)
        # create cancelled event
        startDateTime = create_period("2019-01-11 11:00") # future date
        endDateTime = create_period("2019-01-11 12:00")   # future date
        deregEnd = create_period("2019-01-09 09:00")      # future date
        earlybirdEnd = create_period("2019-01-07 09:00")  # future date
        self.cancelledSeminarId = self.system.addSeminar(self.staff,startDateTime,endDateTime,"cancelledSeminarId","desc",self.venueId7,self.staff,100,deregEnd,2,earlybirdEnd)
        self.cancelledCourseId = self.system.addCourse(self.staff,startDateTime,endDateTime,"cancelledCourseId","desc",self.venueId8,self.staff,100,deregEnd,2,earlybirdEnd)
        self.cancelledSessionId = self.system.addSession(self.staff,self.cancelledSeminarId,startDateTime,endDateTime,"cancelledSessionId","desc",100,self.guest)
        self.system.cancelEvent(self.cancelledSeminarId)
        self.system.cancelEvent(self.cancelledCourseId)
    
    # because you cannot create a closed event, this test was left for client side validation
    def test_invalid_registration_to_closed_event_as_guest(self):
        pass

    def test_valid_reg_to_session_as_guest(self):
        session = self.system.getEvent(self.currSessionId)
        self.system.registerUser(self.currSessionId,self.guestId2)
        assert self.guest2.isRegistered(self.currSessionId) == True
        assert session.hasAttendee(self.guestId2) == True

    def test_valid_reg_to_seminar_as_guest(self):
        seminar = self.system.getEvent(self.currSeminarId)
        self.system.registerUser(self.currSessionId,self.guestId2)
        self.system.registerUser(self.currSeminarId,self.guestId2)
        assert self.guest2.isRegistered(self.currSeminarId) == True
        assert seminar.hasAttendee(self.guestId2) == True
    
    def test_valid_reg_to_course_as_guest(self):
        course = self.system.getEvent(self.currCourseId)
        self.system.registerUser(self.currCourseId,self.guestId2)
        assert self.guest2.isRegistered(self.currCourseId) == True
        assert course.hasAttendee(self.guestId2) == True
    
    def test_valid_dereg_to_session_as_guest(self):
        session = self.system.getEvent(self.currSessionId)
        self.system.registerUser(self.currSessionId,self.guestId2)
        self.system.deregisterUser(self.currSessionId,self.guestId2)
        assert self.guest2.isRegistered(self.currSessionId) == False
        assert session.hasAttendee(self.guestId2) == False
    
    def test_valid_dereg_to_course_as_guest(self):
        course = self.system.getEvent(self.currCourseId)
        self.system.registerUser(self.currCourseId,self.guestId2)
        self.system.deregisterUser(self.currCourseId,self.guestId2)
        assert self.guest2.isRegistered(self.currCourseId) == False
        assert course.hasAttendee(self.guestId2) == False
    
    def test_valid_dereg_to_seminar_as_guest(self):
        seminar = self.system.getEvent(self.currSeminarId)
        self.system.registerUser(self.currSessionId,self.guestId2)
        self.system.registerUser(self.currSeminarId,self.guestId2)
        self.system.deregisterUser(self.currSeminarId,self.guestId2)
        assert self.guest2.isRegistered(self.currSeminarId) == False
        assert seminar.hasAttendee(self.guestId2) == False
    
    def test_guest_is_deregistered_to_all_sessions_of_deregistered_seminar(self):
        session = self.system.getEvent(self.currSessionId)
        self.system.registerUser(self.currSessionId,self.guestId2)
        self.system.registerUser(self.currSeminarId,self.guestId2)
        self.system.deregisterUser(self.currSeminarId,self.guestId2)
        assert self.guest2.isRegistered(self.currSessionId) == False
        assert session.hasAttendee(self.guestId2) == False

    def test_invalid_registration_to_cancelled_event_as_guest(self):
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.cancelledCourseId,self.guestId2)
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.cancelledSeminarId,self.guestId2)

    # because you cannot make an event with a past dereg, this test was tested client side
    def test_invalid_deregistration_after_deregEnd_as_guest(self):
        pass
        
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
        self.fullSeminarId = self.system.addSeminar(self.staff,startDateTime,endDateTime,"fullSeminarId","desc",self.venueId9,self.staff,0,deregEnd,2,earlybirdEnd)
        self.fullCourseId = self.system.addCourse(self.staff,startDateTime,endDateTime,"fullCourseId","desc",self.venueId10,self.staff,0,deregEnd,2,earlybirdEnd)
        self.fullSessionId = self.system.addSession(self.staff,self.fullSeminarId,startDateTime,endDateTime,"fullSessionId","desc",0,self.guest)

        with pytest.raises(RegistrationException):
            self.system.registerUser(self.fullSessionId,self.guestId2)
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.fullCourseId,self.guestId2)

    def test_invalid_registration_to_seminar_without_registering_to_a_session_as_guest(self):
        with pytest.raises(RegistrationException):
            self.system.registerUser(self.currSeminarId, self.guestId2)
    
    # becuase you cannot create an event with a past earlybird date, this test was validated on the client side
    def test_total_registration_fee_is_applied_for_guest(self):
        pass

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

    def test_zero_registration_fee_as_guest_speaker(self):
        assert self.system.getCost(self.currSeminarId,self.guestId) == 0
    
    def test_guest_attendee_is_notified_when_seminar_is_cancelled(self):
        guest = self.system.getUserById(self.guestId2)
        numNotifications = len(guest.getNotificationsMap())
        seminar = self.system.getEvent(self.currSeminarId)
        self.system.registerUser(self.currSessionId,self.guestId2)
        self.system.registerUser(self.currSeminarId,self.guestId2)
        self.system.cancelEvent(self.currSeminarId)
        assert len(guest.getNotificationsMap()) == numNotifications + 1

    def test_guest_attendee_is_notified_when_course_is_cancelled(self):
        guest = self.system.getUserById(self.guestId2)
        numNotifications = len(guest.getNotificationsMap())
        course = self.system.getEvent(self.currCourseId)
        self.system.registerUser(self.currCourseId,self.guestId2)
        self.system.cancelEvent(self.currCourseId)
        assert len(guest.getNotificationsMap()) == numNotifications + 1

    def test_guest_attendee_is_notified_when_session_is_cancelled(self):
        guest = self.system.getUserById(self.guestId2)
        numNotifications = len(guest.getNotificationsMap())
        session = self.system.getEvent(self.currSessionId)
        self.system.registerUser(self.currSessionId,self.guestId2)
        self.system.cancelEvent(self.currSessionId)
        assert len(guest.getNotificationsMap()) == numNotifications + 1
    
    def test_guest_is_notified_when_convener_sets_them_as_presenter_of_session(self):
        numNotifications = len(self.guest.getNotificationsMap())
        startDateTime = create_period("2019-01-11 11:00") # future date
        endDateTime = create_period("2019-01-11 12:00")   # future date
        deregEnd = create_period("2019-01-09 09:00")      # future date
        earlybirdEnd = create_period("2019-01-07 09:00")  # future date
        self.currSeminarId2 = self.system.addSeminar(self.staff,startDateTime,endDateTime,"currSeminar2","desc",self.venueId3,self.staff,100,deregEnd,2,earlybirdEnd)
        self.currSessionId2 = self.system.addSession(self.staff,self.currSeminarId2,startDateTime,endDateTime,"currSession2","desc",100,self.guest)
        assert len(self.guest.getNotificationsMap()) == numNotifications + 1
    
    # this test was validated on the client side becuase route takes care of acceptance
    def test_convener_is_notified_when_guest_accepts_request_to_be_presenter(self):
        pass
    
    # because you cannot create a closed event, his test was validated on the client side
    def test_event_is_moved_to_guests_past_reg_events_if_closed(self):
        pass


# this class tests the guest registration for the main event management system. 
class TestGuestRegistration(object):
    def setup_method(self):
        self.system = bootstrap_system()

    # We do not need to test the actual inputs of add user as these are validated on client side.
    def test_add_valid_new_guest(self):
        guestuser = self.system.addUser("full name","guestuser","test1@mail.com","pass","guest")
        assert self.system.getUserType(guestuser.get_id()) == "Guest"
        assert guestuser.getName() == "full name"
        assert guestuser.get_id() == "guestuser"
        assert guestuser.getPassword() == "pass"

    def test_guest_existing_username(self):
        with pytest.raises(UserExistsException):
            self.system.addUser("full name","guestuser","test1@mail.com","pass","guest")
            self.system.addUser("full name","guestuser","test2@mail.com","pass","guest")
    
    def test_guest_nonexisting_username(self):
            guestuser1 = self.system.addUser("full name","guestuser1","test1@mail.com","pass","guest")
            guestuser = self.system.addUser("full name","guestuser","test2@mail.com","pass","guest") 
            assert self.system.getUserType(guestuser.get_id()) == "Guest"
            assert guestuser.getName() == "full name"
            assert guestuser.get_id() == "guestuser"
            assert guestuser.getEmail() == "test2@mail.com"
            assert guestuser.getPassword() == "pass"   

    def test_guest_existing_email(self):
        with pytest.raises(UserExistsException):
            self.system.addUser("full name","guestuser","test1@mail.com","pass","guest")
            self.system.addUser("full name","guestuser1","test1@mail.com","pass","guest") 

    def test_guest_nonexisting_email(self):
            guestuser1 = self.system.addUser("full name","guestuser1","test1@mail.com","pass","guest")
            guestuser = self.system.addUser("full name","guestuser","test2@mail.com","pass","guest") 
            assert self.system.getUserType(guestuser.get_id()) == "Guest"
            assert guestuser.getName() == "full name"
            assert guestuser.get_id() == "guestuser"
            assert guestuser.getEmail() == "test2@mail.com"
            assert guestuser.getPassword() == "pass"

    def test_guest_existing_email_and_username(self):
        with pytest.raises(UserExistsException):    
            self.system.addUser("full name","guestuser1","test1@mail.com","pass","guest")
            self.system.addUser("full name","guestuser1","test1@mail.com","pass","guest") 

    def test_guest_user_should_be_able_to_login_after_valid_registration_with_username(self):
        self.system.addUser("full name","guestuser1","test1@mail.com","pass","guest")
        user = self.system.getUser("guestuser1")
        assert self.system.checkPassword(user,"pass") == True

    def test_guest_user_should_not_be_able_to_login_after_invalid_registration_with_username(self):
        with pytest.raises(LoginException):    
            try:
                self.system.addUser("full name","guestuser","test2@mail.com","pass","guest")  
                self.system.addUser("full name","guestuser1","test2@mail.com","pass","guest")
            except UserExistsException:
                user = self.system.getUser("guestuser1")
                self.system.checkPassword(user,"pass")
                
    def test_guest_user_should_be_able_to_login_after_valid_registration_with_email(self):
        self.system.addUser("full name","guestuser1","test1@mail.com","pass","guest")
        user = self.system.getUser("test1@mail.com")
        assert self.system.checkPassword(user,"pass") == True

    def test_guest_user_should_not_be_able_to_login_after_invalid_registration_with_email(self):
        with pytest.raises(LoginException):  
            try:
                self.system.addUser("full name","guestuser1","test2@mail.com","pass","guest")  
                self.system.addUser("full name","guestuser1","test1@mail.com","pass","guest")
            except UserExistsException:
                user = self.system.getUser("test1@mail.com")
                self.system.checkPassword(user,"pass")


# this file tests the underlying guest manager class that is used by the main event management system
class TestGuestManagerForGuestRegistration(object):
    def setup_method(self):
        self.guestManager = bootstrap_system().getGuestManager()

    # We do not need to test the actual inputs of add user as these are validated on client side.
    def test_add_valid_new_guest(self):
        guestuser = self.guestManager.addUser("full name","guestuser","test1@mail.com","pass","guest")
        assert self.guestManager.getUserType() == "Guest"
        assert guestuser.getName() == "full name"
        assert guestuser.get_id() == "guestuser"
        assert guestuser.getPassword() == "pass"

    def test_guest_existing_username(self):
        with pytest.raises(UserExistsException):
            self.guestManager.addUser("full name","guestuser","test1@mail.com","pass","guest")
            self.guestManager.addUser("full name","guestuser","test2@mail.com","pass","guest")
    
    def test_guest_nonexisting_username(self):
            guestuser1 = self.guestManager.addUser("full name","guestuser1","test1@mail.com","pass","guest")
            guestuser = self.guestManager.addUser("full name","guestuser","test2@mail.com","pass","guest") 
            assert self.guestManager.getUserType() == "Guest"
            assert guestuser.getName() == "full name"
            assert guestuser.get_id() == "guestuser"
            assert guestuser.getEmail() == "test2@mail.com"
            assert guestuser.getPassword() == "pass"   

    def test_guest_existing_email(self):
        with pytest.raises(UserExistsException):
            self.guestManager.addUser("full name","guestuser","test1@mail.com","pass","guest")
            self.guestManager.addUser("full name","guestuser1","test1@mail.com","pass","guest") 

    def test_guest_nonexisting_email(self):
            guestuser1 = self.guestManager.addUser("full name","guestuser1","test1@mail.com","pass","guest")
            guestuser = self.guestManager.addUser("full name","guestuser","test2@mail.com","pass","guest") 
            assert self.guestManager.getUserType() == "Guest"
            assert guestuser.getName() == "full name"
            assert guestuser.get_id() == "guestuser"
            assert guestuser.getEmail() == "test2@mail.com"
            assert guestuser.getPassword() == "pass"

    def test_guest_existing_email_and_username(self):
        with pytest.raises(UserExistsException):    
            self.guestManager.addUser("full name","guestuser1","test1@mail.com","pass","guest")
            self.guestManager.addUser("full name","guestuser1","test1@mail.com","pass","guest") 
