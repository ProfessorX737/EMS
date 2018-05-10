from src.Student import *
from src.Staff import *
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
        if (role == 'trainee'):
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
        elif userID in self.__staff:
            staff = self.__staff.get(userID)
            staff.removeRegisteredEvent(eventName)
    def cancelEvent(self,convener,eventName):
        for s in self.__staff.values():
            s.cancelRegisteredEvent(eventName)
        for s in self.__students.values():
            s.cancelRegisteredEvent(eventName)
        convener.cancelPostedEvent(eventName)
    def notifyRegistreesNewSession(self,seminarName, sessionName):
        for student in self.__students.values():
            if student.isRegistered(seminarName):
                student.addNotification("A new session " + "'{0}'".format(sessionName) + " was added to " + "'{0}'".format(seminarName) + " seminar")
    def changeRegisteredEvent(self,oldEventName,editedEvent):
        for student in self.__students.values():
            if student.isRegistered(oldEventName):
                student.removeRegisteredEvent(oldEventName)
                student.addRegisteredEvent(editedEvent)
        for staff in self.__staff.values():
            if staff.isRegistered(oldEventName):
                staff.removeRegisteredEvent(oldEventName)
                staff.addRegisteredEvent(editedEvent)
        