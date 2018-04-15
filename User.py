import from Person *
class User(Person):
    def __init__(self,name,zid,email,password):
        super().__init__(name,email)
        self.__zid = zid
        self.__password = password
        self.__currEvents = []
        self.__pastEvents = []
    def zid (self):
        return self.__zid
    def password(self):
        return self.__password
    def currEvents(self):
        return self.__currEvents
    def pastEvents(self):
        return self.__pastEvents
    def setName(self,name):
        self.__name = name
    def setZid(self,zid):
        self.__zid = zid
    def setEmail(self,email):
        self.__email = email
    def setPassword(self,password):
        self.__password = password
    def setCurrEvents(self,currEvents):
        self.__currEvents = currEvents
    def setPastEvents(self,pastEvents):
        sef.__pastEvents = pastEvents