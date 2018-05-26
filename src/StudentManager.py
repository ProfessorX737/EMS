from src.Student import *
from src.Staff import *
from src.Guest import *
from datetime import datetime
from src.UserManager import *
from src.exceptions.UserExistsException import *

class StudentManager(UserManager):
    def __init__(self):
        super().__init__()
    def addUser(self,name,zID,email,password,role):
        user = Student(name,zID,email,password)
        try:
            user = super().addUser(user)
            return user
        except UserExistsException as errMsg:
            raise errMsg
    def getUserType(self):
        return "Student"