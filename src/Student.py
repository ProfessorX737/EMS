from src.User import *
class Student(User):
    def __init__(self,name,userId,email,password):
        super().__init__(name,userId,email,password)


        