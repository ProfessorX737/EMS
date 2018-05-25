from .EventManagementSystem import *
from .Venue import *
from .Guest import *
from .Staff import *
from .Seminar import *
from .Session import *


def bootstrap_system():
    system = EventManagementSystem()

    staff = ems.addUser('Staff name','5123456','staff@mail.com','pw','trainer')
    guest = ems.addUser('Guest name', 'guest', 'guest@mail.com', 'pw', 'guest')

    venue1 = ems.addVenue('venue1', 'somewhere', 100)
    venue1Id = venue1.getId()
    #actually need to get venueId.. but assume 1


    startDateTime = create_period(2018, 01, 01, 11, 00)
    endDateTime = create_period(2018, 01, 31, 13, 00)
    deregEnd = create_period(2018, 01, 30, 00, 00)
    earlybirdEnd = create_period(2018, 01, 15, 07, 00)
    ems.addSeminar(staff,startDateTime,endDateTime,'Seminar One','Some random desc.', venue1Id, staff, 100, deregEnd, 100, earlybirdEnd)

    startDateTime = create_period(2018, 01, 01, 11, 00)
    endDateTime = create_period(2018, 01, 01, 13, 00)
    deregEnd = create_period(2018, 01, 01, 00, 00)
    earlybirdEnd = create_period(2017, 12, 15, 23, 59)
    ems.addSession(staff,seminarId,startDateTime,endDateTime,name,descr,capacity,presenter):

    return system

# helper
def create_period(self, year, month, date, hr, min):
    date_format = "%Y-%m-%d %H:%M"
    date = datetime.strptime("%d-%d-%d %d:%d"(year, month, date, hr, min), date_format)
    return date
