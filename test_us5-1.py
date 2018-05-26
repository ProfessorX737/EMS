from src.EventManagementSystem import *
from src.GuestManager import *
from src.Guest import *
from src.client import *
import pytest

class TestGuestRegistration(object):
    def setup_method(self):
        self.system = bootstrap_system()

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
    
    def test_guest_existing_email(self):
        with pytest.raises(UserExistsException):
            self.system.addUser("full name","guestuser","test1@mail.com","pass","guest")
            self.system.addUser("full name","guestuser1","test1@mail.com","pass","guest") 
