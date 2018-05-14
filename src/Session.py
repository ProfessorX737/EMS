from src.Period import *

class Session(Period):
    def __init__(self,id,startDateTime,endDateTime,name,descr,presenter):
        super().__init__(startDateTime,endDateTime,name,descr)                   # period
        self.__presenter = presenter           # Person
<<<<<<< HEAD

=======
        self.__id = id
    
    def getId(self):
        return self.__id
    
>>>>>>> 7dee702be88734276b69e42f633cd34d60e0d66d
    def getPresenter(self):
        return self.__presenter

    def setPresenter(self,presenter):
        self.__presenter = presenter
