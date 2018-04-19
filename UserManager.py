from Student import *
from Staff import *
from datetime import datetime
class UserManager():
    def __init__(self):
        self.__students = []
        self.__staff = []
    def getStudents(self):
        return self.__students
    def getStaff(self):
        return self.__staff
    def setStaff(self,staff):
        self.__staff =staff
    def setStudents(self,students):
        self.__students = students 
    def getCurrEvents(self,student):
        return student.getCurrEvents()
    def getPastEvents(self,student):
        return student.getPastEvents()
    def getPostedCurrEvents(self,staff):
        return staff.getPostedCurrEvents()
    def getPostedPastEvents(self,staff):
        return staff.getPostedPastEvents()
    def getCancelledEvents(self,staff):
        return staff.getCancelledEvents()
    def addUser(self,name,zID,email,password,role):
        if (role == "trainee"):
            student = Student(name,zID,email,password)
            self.__students.append(student)
        else:
            staff = Staff(name,zID,email,password)
            self.__staff.append(staff)
    def getUser(self,zid):
        for user in self.__students:
            if (user.get_id() == zid):
                return user
        for user in self.__staff:
            if (user.get_id() == zid):
                return user        
    def getUserType(self,zid):
        u = self.getUser(zid)
        print(u.get_id())
        if isinstance(u,Student):
            return "Student"
        else:
            return "Staff"
    def deregister(self,event, user):
        currEvents = user.getCurrEvents()
        for e in currEvents:
            if (e.getName() == event.getName()):
                currEvents.remove(e)
    def register(self,event,user):
        user.getCurrEvents().append(event)
    def postEvent(self,event,staff):
        staff.getPostedCurrEvents().append(event)
    def cancelEvent(self,event,staff):
        staff.getCancelledEvents().append(event)
        staff.getPostedCurrEvents().remove(event)
    def updateEvents(self,event,user):
        currTime = datetime.datetime.now()
        closedEvents = user.getPastEvents()
        currEvents = user.getCurrEvents()
        for e in currEvents:
            if (currTime >= e.getEndDateTime()):
                currEvents.remove(e)
                closedEvents.append(e)
    def updatePostedEvents(self,event,staff):
        currTime = datetime.datetime.now()
        closedEvents = staff.getPostedPastEvents()
        currEvents = staff.getPostedCurrEvents()
        for e in currEvents:
            if (currTime >= e.getEndDateTime()):
                currEvents.remove(e)
                closedEvents.append(e)