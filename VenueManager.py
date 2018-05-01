from Venue import *

class VenueManager():
    def __init__(self):
        self.__venues = {}

    def addVenue(self, name, loc, capacity):
        if name not in self.__venues:
            venue = Venue(name,loc,capacity)
            self.__venues[name] = venue
            return True
        return False

    def removeVenue(self, name):
        del self.__venues[name]

    def getVenues(self):
        print(self.__venues.values())
        return self.__venues.values()

    def getVenueNames(self):
        return self.__venues

    def getFreeTimes(self, name):
        return self.__venues[name].getFreePeriods()
