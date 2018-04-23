from EventManager import *
from Course import *
class CourseManager(EventManager):
    def __init__(self):
        super().__init__()
    def addCourse(self,startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd):
        course = Course(startDateTime, endDateTime, name, descr, venue, convener, capacity, deregEnd)
        self.addEvent(course)