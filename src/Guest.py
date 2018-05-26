from src.User import *
from src.Presenter import *

class Guest(Presenter):
    def __init__(self,name,zid,email,password):
        super().__init__(name,zid,email,password)