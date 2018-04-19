from Seminar import *
class EventManager():
    def __init__(self):
        self.__events = {}
    def getEvents(self):
        return self.__events
    def addAttendee(eventName, user):
        exits = False;
        for e in self.__events:
            if (e.getName() == eventName):
                isConfirmed = e.addAttendee(user)
    def addEvent(self,event):
        self.__events.append(event)