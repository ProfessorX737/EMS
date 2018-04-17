from Event import *
from User import *

class EventManager():
    def __init__(self):
        self._venues : []
        self._events: []
    
    def getVenues(self):
        return self._venues
        
    def getEvents(self):
        return self._events
  
    def addVenue(self, venue):
        self._venues.append(venue)
    
    def addEvent(self, event):
        self._events.append(event)
        
    def addAttendee(self, event, attendee):
        for x in self._events:
            if (x == event):
                return x.addAttendee(attendee)
            
    # what is this function supposed to do???
    def changeEvent(self, event):
        pass
        
        
    def getVenue(self, event):
        for x in self._events:
            if (x == event):
                return x.getVenue
