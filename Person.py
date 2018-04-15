class Person():
    def __init__(self,name,email):
        self.__name = name
        self.__email = email
    def name(self):
        return self.__name
    def email(self):
        return self.__email
    def setName(self, name):
        self.__name = name
    def setEmail(self,email):
        self.__email = email
