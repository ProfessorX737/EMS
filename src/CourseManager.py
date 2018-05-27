from src.EventManager import *
from src.Course import *
from src.exceptions.InvalidEventDateException import *
class CourseManager(EventManager):
    def __init__(self):
        super().__init__()
    def addCourse(self,course):
        try:
            return self.addEvent(course)
        except InvalidEventDateException as errMsg:
            raise errMsg