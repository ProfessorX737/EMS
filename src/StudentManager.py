from src.Student import *
from src.Staff import *
from src.Guest import *
from datetime import datetime
from src.UserManager import *

class StudentManager(UserManager):
    def __init__(self):
        super().__init__()

    def getUserType(self):
        return "Student"