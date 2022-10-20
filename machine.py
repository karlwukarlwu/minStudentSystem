from student import Student
from course import Course
from admin import Admin

class Machine:
    def __init__(self):
        self.end = 100

    def find_student(self,num,*students:Student):
        for stu in students:
            if num == stu.stuNum:
                return stu
        return "notIn"


    def find_students(self):
        self
