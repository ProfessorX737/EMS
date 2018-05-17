from src.Period import *

class Session(Period):
    def __init__(self,id,startDateTime,endDateTime,name,descr,presenter):
        super().__init__(startDateTime,endDateTime,name,descr)                   # period
        self.__presenter = presenter           # Person
        self.__id = id

    def getId(self):
        return self.__id

    def getPresenter(self):
        return self.__presenter

    def setPresenter(self,presenter):
        self.__presenter = presenter
