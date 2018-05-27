from src.EventManagementSystem import *
from src.Guest import *
from src.client import *
import pytest

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