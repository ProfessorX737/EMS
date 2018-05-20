from src.Student import *
from src.Staff import *
from src.Guest import *
from datetime import datetime
from src.UserManager import *

class StudentManager(UserManager):
    def __init__(self):
        self.__students = {}
    def getUsers(self):
        return self.__students.values()
    def setUsers(self,users):
        for u in users:
            self.__students[u.get_id()] = u
    def addUser(self,name,zID,email,password,role):
        if zID not in self.__students:
            student = Student(name,zID,email,password)
            self.__students[student.get_id()] = student
            return True
        return False
    def getUserById(self,zid):
        if zid in self.__students:
            return self.__students.get(zid)
        else:
            return None
    def getUserByEmail(self,email):
        for user in self.__students.values():
            if user.getEmail() == email:
                return user
        return None
    def getUserType(self):
        return "Student"
    def addRegisteredEvent(self,userID,event):
        if userID in self.__students:
            self.__students[userID].addRegisteredEvent(event)
    def removeRegisteredEvent(self,userID,eventId):
        if userID in self.__students:
            student = self.__students.get(userID)
            student.removeRegisteredEvent(eventId)
    def cancelEvent(self,eventId):
        for s in self.__students.values():
            s.cancelRegisteredEvent(eventId)
    def notifyRegistrees(self,eventId,notification):
        for student in self.__students.values():
            if student.isRegistered(eventId):
                student.addNotification(notification)
    def notifyRegistreesNewSession(self,seminarId, seminarName, sessionName):
        for student in self.__students.values():
            if student.isRegistered(seminarId):
                student.addNotification("A new session '{0}' was added to '{1}' seminar".format(sessionName,seminarName))
    def notifyRegistreesEventEdit(self, eventId):
        for student in self.__students.values():
            if student.isRegistered(eventId):
                student.addNotification("The details of '{0}' event were changed".format(student.getRegisteredEventName(eventId))) 
    def changeRegisteredEvent(self,oldEventId,editedEvent):
        for student in self.__students.values():
            if student.isRegistered(oldEventId):
                student.removeRegisteredEvent(oldEventId)
                student.addRegisteredEvent(editedEvent)