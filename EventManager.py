from Seminar import *
class EventManager():
    def __init__(self):
        self.__venues = []
        self.__events = []
    def getEvents(self):
        return self.__events
    def getVenues(self):
        return self.__venues
    def addVenue(self,venue):
        if (venue not in self.__venues):
            self.__venues.append(venue)
            return True
        else:
            return False
    def addSession(self,seminar,session):
        seminar.addSession(session)
    def addAttendee(eventName, user):
        for e in self.__events:
            if (e.getName() == eventName):
                isConfirmed = e.addAttendee(user)
            if isConfirmed:
                return True
            else:
                return False
    def addEvent(self,event):
        events.append(event)