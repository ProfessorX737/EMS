from src.User import *

class Guest(User):
    def __init__(self,name,zid,email,password):
        super().__init__(name,zid,email,password)
