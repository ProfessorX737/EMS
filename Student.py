from User import *
class Student(User):
    def __init__(self,name,zid,email,password,isAuthenticated,isActive,isAnonymous):
        super().__init__(name,zid,email,password,isAuthenticated,isActive,isAnonymous)


        