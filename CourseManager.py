from EventManager import *
from Course import *
class CourseManager(EventManager):
    def __init__(self):
        super().__init__()
    def addCourse(self,course):
        self.addEvent(course)