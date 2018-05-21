from src.Staff import *
from src.Guest import *
from src.UserManager import *
from datetime import datetime

class GuestManager(UserManager):
    def __init__(self):
        super().__init__()
        
    def getUserType(self):
        return "Guest"
