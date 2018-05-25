from src.EventManagementSystem import *
from src.GuestManager import *
from src.Guest import *
from Server import ems
import pytest

user = ems.addUser("name 0","guest","test0@mail.com","pass","guest")

def test_new_guest():
    print("test new guest")
    ems.addUser("full name","guestuser","test1@mail.com","pass","guest")
    assert ems.userIdExists(guestuser)
    assert ems.getUserType(guestuser) == "Guest"
    user1 = ems.getUserById(guestuser)
    assert user1.getName() == "full name"
    assert user1.getId() == "guestuser"

def test_guest_existing_username():
    print("test preexisting username")
    ems.addUser("full name","guest","test2@mail.com","pass","guest")

# ems and form already have their own set of errors for invalid input?
def test_guest_existing_email():
    print("test preexisting email")
    ems.addUser("fuller name","guestuser2","test0@mail.com","pass","guest")
    #with pytest.raises(RegisterException):
        #ems.addUser("name 3","guest3","test2@mail.com","pass","guest")


def test_guest_existing_fullname():
    print("test new guest w/ preexisting FULL NAME")
    ems.addUser("full name","guestuser3","test3@mail.com","pass","guest")
    assert ems.userIdExists(guestuser3)
    assert ems.getUserType(guestuser3) == "Guest"
    user3 = ems.getUserById(guestuser3)
    assert user3.getName() == "full name"
    assert user3.getId() == "guestuser3"
