from Venue import *

class VenueManager():
    def __init__(self):
        self.__venues = {}

    def addVenue(self, name, loc):
        self.__venues[name] = loc

    def removeVenue(self, name):
        self.__venues.pop(name)

    def getVenues(self):
        return self.__venues

    def getFreeTimes(self, name):
        return self.__venues[name].getFreePeriods()
