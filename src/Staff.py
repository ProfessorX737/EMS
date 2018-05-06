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
            self.__postedCurrEvents[e.getName()] = e
    def setPostedPastEvents(self,postedPastEvents):
        for e in postedPastEvents:
            self.__postedPastEvents[e.getName()] = e
    def setCancelledEvents(self,cancelledEvents):
        for e in cancelledEvents:
            self.__cancelledEvents[e.getName()] = e
    def addPostedCurrEvent(self,event):
        self.__postedCurrEvents[event.getName()] = event
    def cancelPostedEvent(self,eventName):
        if eventName in self.__postedCurrEvents:
            self.__cancelledEvents.append(self.__postedCurrEvents[eventName])
            del self.__postedCurrEvents[eventName] 
        elif eventName in self.__postedPastEvents:
            self.__cancelledEvents.append(self.__postedPastEvents[eventName])
            del self.__postedPastEvents[eventName] 
