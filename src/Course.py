from src.Event import Event

class Course(Event):
    def __init__(self,id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,fee,earlybirdEnd):
        super().__init__(id,startDateTime,endDateTime,name,descr,venue,convener,capacity,deregEnd,fee,earlybirdEnd)
    
    def getPresenter(self):
        return self.getConvener()

    def getClassName(self):
        return "Course"