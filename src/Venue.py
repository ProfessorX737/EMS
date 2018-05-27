
class Venue:
    def __init__(self,id,name,location,maxCapacity):
        self._name = name
        self._id = id
        self._location = location
        self._maxCapacity = maxCapacity
        self._periods = {}
    def getId(self):
        return self._id
    def getName(self):
        return self._name
    def getLocation(self):
        return self._location
    def getMaxCapacity(self):
        return self._maxCapacity
    def setName(self,name):
        self._name = name
    def setLocation(self,location):
        self._location = location
    def setMaxCapacity(self,maxCapacity):
        self._maxCapacity = maxCapacity
    def getPeriodIds(self):
        return self._periods
    def getPeriods(self):
        return self._periods.values()
    def addPeriod(self,period):
        if period.getId() not in self._periods and not self.overlaps(period):
            self._periods[period.getId()] = period
            return True
        return False
    def overlaps(self,period):
        for p in self.getPeriods():
            if p.getStartDateTime() <= period.getEndDateTime() \
                and p.getEndDateTime() >= period.getStartDateTime():
                return True
        return False
            # (StartA <= EndB) and (EndA >= StartB)

    def deletePeriod(self,periodId):
        if periodId in self._periods:
            del self._periods[periodId]

        


