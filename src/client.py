from .EventManagementSystem import *
from .Venue import *
from .Guest import *
from .Staff import *
from .Seminar import *
from .Session import *

def create_period(date):
    date_format = "%Y-%m-%d %H:%M"
    date = datetime.datetime.strptime(date, date_format)
    return date

def bootstrap_system():
    system = EventManagementSystem()

    staff = system.addUser('Staff name','5123456','staff@mail.com','pw','trainer')
    guest = system.addUser('Guest name', 'guest', 'guest@mail.com', 'pw', 'guest')

    venue1 = system.addVenue('venue1', 'somewhere', 100)
    venue1Id = venue1.getId()
    #actually need to get venueId.. but assume 1
    

    startDateTime = create_period("2019-01-11 11:00")
    endDateTime = create_period("2019-01-11 12:00")
    deregEnd = create_period("2019-01-09 09:00")
    earlybirdEnd = create_period("2019-01-07 09:00")
    system.addSeminar(staff,startDateTime,endDateTime,'Seminar One','Some random desc.', venue1Id, staff, 100, deregEnd, 100, earlybirdEnd)

    # startDateTime = create_period(2018, 01, 01, 11, 00)
    # endDateTime = create_period(2018, 01, 01, 13, 00)
    # deregEnd = create_period(2018, 01, 01, 00, 00)
    # earlybirdEnd = create_period(2017, 12, 15, 23, 59)
    # ems.addSession(staff,seminarId,startDateTime,endDateTime,name,descr,capacity,presenter):

    return system

# helper

