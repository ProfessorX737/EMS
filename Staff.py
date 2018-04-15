from User import *
class Staff(User):
    def __init__(self,name,zid,email,password):
        super().__init__(name,zid,email,password)
        self.__postedCurrEvents = []
        self.__postedPastEvents = []
        self.__cancelledEvents = []
    def postedCurrEvents(self):
        return self.__postedCurrEvents
    def postedPastEvents(self):
        return self.__postedPastEvents
    def cancelledEvents(self):
        return self.__cancelledEvents
    def setPostedCurrEvents(self,postedCurrEvents):
        self.__postedCurrEvents = postedCurrEvents
    def setPostedPastEvents(self,postedPastEvents):
        self.__postedPastEvents = postedPastEvents
    def setCancelledEvents(self,cancelledEvents):
        self.__cancelledEvents = cancelledEvents
    

