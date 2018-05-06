class Person():
    def __init__(self,name,email):
        self.__name = name
        self.__email = email
    def getName(self):
        return self.__name
    def getEmail(self):
        return self.__email
    def setName(self, name):
        self.__name = name
    def setEmail(self,email):
        self.__email = email
