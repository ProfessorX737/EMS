from Event import *
from Session import *

class Seminar(Event):
    def __init__(self,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd):
        super().__init__(startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd)
        self.__sessions = []

    #def addSession()