
class Period:
    def __init__(self, name, des, loc, startDate, endDate, startTime, endTime):
        self._name = name
        self._des = des
        self._loc = loc
        self._startDate = startDate
        self._endDate = endDate
        self._startTime = startTime
        self._endTime = endTime
    
    def getName(self):
        return self._name
    def getDes(self):
        return self._des
    def getLoc(self):
        return self._loc
    def getStartDate(self):
        return self._startDate
    def getEndDate(self):
        return self._endDate
    def getStartTime(self):
        return self._startTime
    def getEndTime(self):
        return self._endTime

    def setName(self,name):
        self._name = name
    def setDes(self, des):
        self._des = des
    def setLoc(self,loc):
        self._loc = loc
    def setStartDate(self,startDate):
        self._startDate = startDate
    def setEndDate(self, endDate):
        self._endDate = endDate
    def setStartTime(self, startTime):
        self._startTime = startTime
    def setEndTime(self,endTime):
        self._endTime = endTime
        
    

        