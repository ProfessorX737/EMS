from src.Venue import *
from src.exceptions.ExistingVenueException import *
class VenueManager():
    def __init__(self):
        self.__venues = {}
    def addVenue(self,id,name, loc, capacity):
        if id not in self.__venues:
            id = self._getUniqueVenueId()
            venue = Venue(id,name,loc,capacity)
            self.__venues[id] = venue
            return venue
        else:
            raise ExistingVenueException('Venue','Venue with this name already exists')
    def getIdByName(self,name):
        for v in self.__venues.values():
            if v.getName() == name:
                return v.getId()
        return None
            
    def removeVenue(self, venueId):
        del self.__venues[venueId]
    def getVenues(self):
        return self.__venues.values()
    def getVenue(self,venueId):
        if venueId in self.__venues:
            return self.__venues[venueId]
        return None
    def getVenueNames(self):
        venueNames = []
        for v in self.__venues.values():
            venueNames.append(v.getName())
        return venueNames
    def getFreeTimes(self, venueId):
        return self.__venues[venueId].getFreePeriods()
    def venueContainsPeriodId(self,venueId,periodId):
        venue = self.__venues[venueId]
        if periodId in venue.getPeriodIds():
            return True
        return False
    def _getUniqueVenueId(self):
        id = 0
        while id in self.__venues:
            id = id + 1
        return id