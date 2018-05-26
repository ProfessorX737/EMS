from src.EventManagementSystem import *
from src.GuestManager import *
from src.Guest import *
from src.client import *
import pytest

class TestGuestRegistration(object):
    def setup_method(self):
        self.system = bootstrap_system()

    def test_add_valid_new_guest():
        self.system.addUser("full name","guestuser","test1@mail.com","pass","guest")
        assert self.system.getUserType(guestuser) == "Guest"
        user1 = self.system.getUserById(guestuser)
        assert user1.getName() == "full name"
        assert user1.getId() == "guestuser"
        assert user1.getPassword() == "pass"

    def test_guest_existing_username():
        with pytest.raises(UserExistsException):
            self.system.addUser("full name","guestuser","test2@mail.com","pass","guest")
    
    def test_guest_existing_email():
        with pytest.raises(UserExistsException):
            self.system.addUser("full name","guestuser1","test1@mail.com","pass","guest")

    def test_guest_existing_fullname():
        self.system.addUser("full name","guestuser3","test3@mail.com","pass","guest")
        assert self.system.userIdExists(guestuser3)
        assert self.system.getUserType(guestuser3) == "Guest"
        user3 = self.system.getUserById(guestuser3)
        assert user3.getName() == "full name"
        assert user3.getId() == "guestuser3"
