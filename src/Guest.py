from src.User import *
from src.Presenter import *

class Guest(Presenter):
    def __init__(self,name,userId,email,password):
        super().__init__(name,userId,email,password)