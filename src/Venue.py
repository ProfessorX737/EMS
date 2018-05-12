
class Venue:
    def __init__(self,id,name,location,maxCapacity):
        self._name = name
        self._id = id
        self._location = location
        self._maxCapacity = maxCapacity
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
        


