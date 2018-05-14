from src.Period import *

class Session(Period):
    def __init__(self,seminarName,startDateTime,endDateTime,name,descr,presenter):
        super().__init__(startDateTime,endDateTime,name,descr)                   # period
        self.__presenter = presenter           # Person

    def getPresenter(self):
        return self.__presenter

    def setPresenter(self,presenter):
        self.__presenter = presenter
