from src.Student import *
from src.Staff import *
from src.Guest import *
from datetime import datetime
class UserManager():
    def __init__(self):
        self.__students = {}
        self.__staff = {}
        self.__guest = {}
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
            return True
        elif (role == 'trainer'):
            staff = Staff(name,zID,email,password)
            self.__staff[staff.get_id()] = staff
            return True
        elif (role == 'guest'):
            guest = Guest(name,zID,email,password)
            self.__guest[guest.get_id()] = guest
            return True
        else:
            return False
    def getUser(self,zid):
        if zid in self.__students:
            return self.__students.get(zid)
        if zid in self.__staff:
            return self.__staff.get(zid)
        if zid in self.__guest:
            return self.__guest.get(zid)
    def getUserType(self,zid):
        u = self.getUser(zid)
        if isinstance(u,Student):
            return "Student"
        elif isinstance(u,Staff):
            return "Staff"
        else:
<<<<<<< HEAD
            return None

=======
            return "Guest"
>>>>>>> guest
    def addRegisteredEvent(self,userID,event):
        if userID in self.__students:
            self.__students[userID].addRegisteredEvent(event)
        if userID in self.__staff:
            self.__staff[userID].addRegisteredEvent(event)
    def removeRegisteredEvent(self,userID,eventId):
        if userID in self.__students:
            student = self.__students.get(userID)
            student.removeRegisteredEvent(eventId)
        elif userID in self.__staff:
            staff = self.__staff.get(userID)
            staff.removeRegisteredEvent(eventId)
    def cancelEvent(self,convener,eventId):
        for s in self.__staff.values():
            s.cancelRegisteredEvent(eventId)
        for s in self.__students.values():
            s.cancelRegisteredEvent(eventId)
        convener.cancelPostedEvent(eventId)
    def notifyRegistreesNewSession(self,seminarId, seminarName, sessionName):
        for student in self.__students.values():
            if student.isRegistered(seminarId):
                student.addNotification("A new session '{0}' was added to '{1}' seminar".format(sessionName,seminarName))
        for staff in self.__staff.values():
            if staff.isRegistered(seminarId):
                staff.addNotification("A new session '{0}' was added to '{1}' seminar".format(sessionName,seminarName))
    def notifyRegistreesEventEdit(self, eventId):
        for student in self.__students.values():
            if student.isRegistered(eventId):
                student.addNotification("The details of '{0}' event were changed".format(student.getRegisteredEventName(eventId)))
        for staff in self.__staff.values():
            if staff.isRegistered(eventId):
                student.addNotification("The details of '{0}' event were changed".format(staff.getRegisteredEventName(eventId)))
    def changeRegisteredEvent(self,oldEventId,editedEvent):
        for student in self.__students.values():
            if student.isRegistered(oldeventId):
                student.removeRegisteredEvent(oldEventId)
                student.addRegisteredEvent(editedEvent)
        for staff in self.__staff.values():
            if staff.isRegistered(oldEventId):
                staff.removeRegisteredEvent(oldEventId)
                staff.addRegisteredEvent(editedEvent)
