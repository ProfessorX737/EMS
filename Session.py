from Period import *

class Session(Period):
    def __init__(self,period,presenter):
        super().copy(period)                   # period
        self.__presenter = presenter           # Person
    
    def getPresenter(self):
        return self.__presenter

    def setPresenter(self,presenter):
        self.__presenter = presenter