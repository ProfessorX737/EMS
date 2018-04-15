from Event import *
from Session import *

class Seminar(Event):
    def __init__(self,period,venue,convener,capacity,deregEnd):
        super().__init__(self,period,venue,convener,capacity,deregEnd)
        self.__sessions = []

    #def addSession()