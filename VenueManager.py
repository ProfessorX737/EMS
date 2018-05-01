from Venue import *

class VenueManager():
    def __init__(self):
        self.__venues = {}

    def addVenue(self, name, loc, capacity):
        venue = Venue(name,loc,capacity)
        print(venue)
        self.__venues[name] = venue

    def removeVenue(self, name):
        del self.__venues[name]

    def getVenues(self):
        return self.__venues

    def getFreeTimes(self, name):
        return self.__venues[name].getFreePeriods()
