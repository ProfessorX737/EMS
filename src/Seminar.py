from src.Event import Event

class Seminar(Event):
    def __init__(self,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd):
        super().__init__(startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd)
        self.__sessions = []

    def addSession(self,session):
        for i in self.__sessions:
            if i.getStartDateTime != session.getStartDateTime:
                self.__sessions.append(session)
                print("ADDED SESSION", session.getName())

    def getSessions(self):
        return self.__sessions

    def getClassName(self):
        return "Seminar"
