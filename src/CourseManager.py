from src.EventManager import *
from src.Course import *
class CourseManager(EventManager):
    def __init__(self):
        super().__init__()
    def addCourse(self,course):
        return self.addEvent(course)