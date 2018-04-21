from CourseManager import *
from SeminarManager import *
from UserManager import *
# from VenueManager import *

class EventManagementSystem():
    def __init__(self):
        self.__courseManager = CourseManager()
        self.__seminarManager = SeminarManager()
        self.__userManager = UserManager()
        # venueManager = VenueManager()

    def addCourse(self,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd):
        self.__courseManager.addCourse(startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd)

    def addSeminar(self,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd):
        self.__seminarManager.addSeminar(startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd)
    def getSession(self,seminarName,sessionName):
        self.__seminarManager.getSession(seminarName,sessionName)

    def getStudents(self):
        return self.__userManager.getStudents()
    def getStaff(self):
        return self.__userManager.getStaff()
    def setStaff(self,staff):
        self.__userManager.setStaff(staff)
    def setStudents(self,students):
        self.__userManager.setStudents(students)
    def getCurrEvents(self,user):
        return self.__userManager.getCurrEvents(user)
    def getPastEvents(self,user):
        return self.__userManager.getPastEvents(user)
    def getPostedCurrEvents(self,staff):
        return self.__userManager.getPostedCurrEvents(staff)
    def getPostedPastEvents(self,staff):
        return self.__userManager.getPostedPastEvents(staff)
    def getCancelledEvents(self,staff):
        return self.__userManager.getCancelledEvents(staff)
    def addUser(self,name,zID,email,password,role):
        self.__userManager.addUser(name,zID,email,password,role)
    def getUser(self,zid):
        return self.__userManager.getUser(zid) 
    def getUserType(self,zid):
        return self.__userManager.getUserType(zid)

    # venue manager methods below