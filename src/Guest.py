from src.User import *

class Guest(User):
    def __init__(self,name,zid,email,password):
        super().__init__(name,zid,email,password)
        self.__sessions = {}
    def addSession(self, session):
        self.__sessions[session.getId()] = session
    def getSession(self, sessionId):
        if sessionId in self.__sessions:
            return self.__sessions[sessionId]
        return None
    def getSessions(self):
        return self.__sessions.values()
    # def isMyEvent(self,eventId):
        # return False
        # if eventId in self.__sessions:
        #     return True
        # return False

