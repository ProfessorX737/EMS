from User import *

class Guest(Person):
    def __init__(self,name,zid,email,password):
        super().__init__(name,zid,email,password)
