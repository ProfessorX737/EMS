from src.Event import Event

class Course(Event):
    def __init__(self,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd):
        super().__init__(startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd)
    
    def getPresenter(self):
        return self.getConvener()

    def getClassName(self):
        return "Course"