from src.User import *
class Staff(User):
    def __init__(self,name,zid,email,password):
        super().__init__(name,zid,email,password)
        self.__postedCurrEvents = {}
        self.__postedPastEvents = {}
        self.__cancelledEvents = []
    def getPostedCurrEvents(self):
        return self.__postedCurrEvents.values()
    def getPostedPastEvents(self):
        return self.__postedPastEvents.values()
    def getCancelledEvents(self):
        return self.__cancelledEvents
    def setPostedCurrEvents(self,postedCurrEvents):
        for e in postedCurrEvents:
            self.__postedCurrEvents[e.getId()] = e
    def setPostedPastEvents(self,postedPastEvents):
        for e in postedPastEvents:
            self.__postedPastEvents[e.getId()] = e
    def setCancelledEvents(self,cancelledEvents):
        for e in cancelledEvents:
            self.__cancelledEvents[e.getId()] = e
    def addPostedCurrEvent(self,event):
        self.__postedCurrEvents[event.getId()] = event
    def cancelPostedEvent(self,eventId):
        if eventId in self.__postedCurrEvents:
            self.__cancelledEvents.append(self.__postedCurrEvents[eventId])
            del self.__postedCurrEvents[eventId] 
        elif eventId in self.__postedPastEvents:
            self.__cancelledEvents.append(self.__postedPastEvents[eventId])
            del self.__postedPastEvents[eventId] 
