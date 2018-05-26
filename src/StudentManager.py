from src.Student import *
from src.Staff import *
from src.Guest import *
from datetime import datetime
from src.UserManager import *

class StudentManager(UserManager):
    def __init__(self):
        super().__init__()
    def addUser(self,name,userId,email,password,role):
        user = Student(name,userId,email,password)
        super().addUser(user)
    def getUserType(self):
        return "Student"