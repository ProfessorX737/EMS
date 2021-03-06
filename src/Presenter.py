from src.User import *

class Presenter(User):
    def __init__(self,name,userId,email,password):
        super().__init__(name,userId,email,password)
        self.__sessions = {}
    def addSession(self, session):
        self.__sessions[session.getId()] = session
    def getSession(self, sessionId):
        if sessionId in self.__sessions:
            return self.__sessions[sessionId]
        return None
    def isPresenter(self,sessionId):
        if sessionId in self.__sessions:
            return True
        return False
    def getSessions(self):
        return self.__sessions.values()
    def deleteSession(self,sessionId):
        if sessionId in self.__sessions:
            del self.__sessions[sessionId]