from src.Venue import *

class VenueManager():
    def __init__(self):
        self.__venues = {}
    def addVenue(self,name, loc, capacity):
        if name not in self.__venues:
            id = self._getUniqueVenueId()
            venue = Venue(id,name,loc,capacity)
            self.__venues[id] = venue
            return True
    def removeVenue(self, venueId):
        del self.__venues[venueId]
    def getVenues(self):
        return self.__venues.values()
    def getVenue(self,venueName):
        for v in self.__venues.values():
            if v.getName() == venueName:
                return v
        return None
    def getVenueNames(self):
        venueNames = []
        for v in self.__venues.values():
            venueNames.append(v.getName())
        return venueNames
    def getFreeTimes(self, venueId):
        return self.__venues[venueId].getFreePeriods()
    def _getUniqueVenueId(self):
        id = 0
        while id in self.__venues:
            id = id + 1
        return id