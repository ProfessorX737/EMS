from Student import *
from Staff import *
from datetime import datetime
class UserManager():
    def __init__(self):
        self.__students = {}
        self.__staff = {}
    def getStudents(self):
        return self.__students.values()
    def getStaff(self):
        return self.__staff.values()
    def setStaff(self,staff):
        for s in staff:
            self.__staff[s.get_id()] = s
    def setStudents(self,students):
        for s in students:
            self.__students[s.get_id()] = s
    def getCurrEvents(self,user):
        return user.getCurrEvents()
    def getPastEvents(self,user):
        return user.getPastEvents()
    def getPostedCurrEvents(self,staff):
        return staff.getPostedCurrEvents()
    def getPostedPastEvents(self,staff):
        return staff.getPostedPastEvents()
    def getCancelledEvents(self,staff):
        return staff.getCancelledEvents()
    def addUser(self,name,zID,email,password,role):
        if (role == "trainee"):
            student = Student(name,zID,email,password)
            self.__students[student.get_id()] = student
        else:
            staff = Staff(name,zID,email,password)
            self.__staff[staff.get_id()] = staff
    def getUser(self,zid):
        if zid in self.__students:
            return self.__students.get(zid)
        if zid in self.__staff:
            return self.__staff.get(zid)
    def getUserType(self,zid):
        u = self.getUser(zid)
        print(u.get_id())
        if isinstance(u,Student):
            return "Student"
        else:
            return "Staff"
    def addRegisteredEvent(self,userID,event):
        if userID in self.__students:
            self.__students[userID].addRegisteredEvent(event)
        if userID in self.__staff:
            self.__staff[userID].addRegisteredEvent(event)
    def removeRegisteredEvent(self,userID,eventName):
        if userID in self.__students:
            student = self.__students.get(userID)
            student.removeRegisteredEvent(eventName)