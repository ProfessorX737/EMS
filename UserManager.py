from Student import *
from Staff import *
class UserManager():
    def __init__(self,students,staff):
        self.__students = students
        self.__staff = staff
    def students(self):
        return self.__students
    def staff(self):
        return self.__staff
    def setStaff(self,staff):
        self.__staff =staff
    def setStudents(self,students):
        self.__students = students 
    def getCurrEvents(student):
        return student.currEvents()
    def getPastEvents(student):
        return student.pastEvents()
    def getPostedCurrEvents(staff):
        return staff.postedCurrEvents()
    def getPostedPastEvents(staff):
        return staff.postedPastEvents()
    def getCancelledEvents(staff):
        return staff.cancelledEvents()
    def addUser(self,name,zID,email,password,role):
        if (role == "trainee"):
            student = Student(name,zID,email,password)
            self.__students.append(student)
        else
            staff = Staff(name,zID,email,password)
            self.__staff.append(staff)