from Event import Event

class Seminar(Event):
    def __init__(self,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd):
        super().__init__(startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd)
        self.__sessions = []

    def addSession(self,session):
        self.__sessions.append(session)
    
    def getClassName(self):
        return "Seminar"