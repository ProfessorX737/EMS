from Person import *
class User(Person):
    def __init__(self,name,zid,email,password):
        super().__init__(name,email)
        self.__zid = zid
        self.__password = password
        self.__currEvents = []
        self.__pastEvents = []
        self.isAuthenticated = False
        self.isActive = False
        self.isAnonymous = False
    def getPassword(self):
        return self.__password
    def getCurrEvents(self):
        return self.__currEvents
    def getPastEvents(self):
        return self.__pastEvents
    # Flask login module required functions
    def get_id(self):
        return self.__zid
    def is_authenticated(self):
        return self.__isAuthenticated
    def is_active(self):
        return self.__isActive
    def is_anonymous(self):
        return self.__isAnonymous
    def set_authenticated(self,isAuthenticated):
        self.__isAuthenticated = isAuthenticated
    def set_active(self,isActive):
        self.__isActive = isActive
    def set_anonymous(self,isAnonymous):
        self.__isAnonymous = isAnonymous
    # end
    def setName(self,name):
        self.__name = name
    def setId(self,zid):
        self.__zid = zid
    def setEmail(self,email):
        self.__email = email
    def setPassword(self,password):
        self.__password = password
    def setCurrEvents(self,currEvents):
        self.__currEvents = currEvents
    def setPastEvents(self,pastEvents):
        self.__pastEvents = pastEvents