from src.EventManagementSystem import *
from src.Venue import *
from src.Guest import *
from src.Staff import *
from src.Seminar import *
from src.Session import *
import pytest

curr_sem = ems.getSessions

class TestRegisterToEvent(object):
    def setup_method(self):
        self.system = bootstrap_system()

    # This test was validated on the client side
    def test_registration_to_closed_event():
        pass

    def test_open_registered_event_in_users_open_events_list():
        pass
    
    def test_past_registered_event_in_users_past_event_list():
        pass

def create_period(self, year, month, date, hr, min):
    date_format = "%Y-%m-%d %H:%M"
    date = datetime.strptime("%d-%d-%d %d:%d"%(year, month, date, hr, min), date_format)
    return

##########GUEST EVENT REGISTRATION
# Tests for seminar registration
def test_seminar_valid():
    print("test_seminar_valid")
    assert ems.registerUserToSeminar(curr_sem[0],user)==True

def test_seminar_exceed_max_capacity():

def test_seminar_closed():

def test_seminar_cancelled():
    pass

def test_seminar_after_dereg():
    pass

# Tests for session registration
def test_session_valid():

def test_session_exceed_max_capacity():

def test_session_closed():

def test_session_cancelled():

def test_session_after_dereg():
    pass

def test_after_early_bird():
    # fee
    pass

def test_before_early_bird():
    # fee discounted 50%
    pass

def test_is_speaker():
    # cant register
    pass
