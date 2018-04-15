from Event import Event
from Session import Session

class Seminar(Event):
    def __init__(self,period,venue,convener,capacity,deregEnd):
        super().__init__(self,period,venue,convener,capacity,deregEnd)
        self.__sessions = []

    #def addSession()