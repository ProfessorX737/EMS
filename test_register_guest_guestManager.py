from src.GuestManager import *
from src.Guest import *
from src.client import *
import pytest

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
