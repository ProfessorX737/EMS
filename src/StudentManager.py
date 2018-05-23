from src.Student import *
from src.Staff import *
from src.Guest import *
from datetime import datetime
from src.UserManager import *

class StudentManager(UserManager):
    def __init__(self):
        super().__init__()
    def addUser(self,name,zID,email,password,role):
        if zID not in self.__users:
            user = Student(name,zID,email,password)
            self.__users[user.get_id()] = user
            return True
    def getUserType(self):
        return "Student"