class Student:
    def __init__(self,student_id,name):
        self.student_id=student_id
        self.name=name
        self.courses={}

    def add_courses(self,course,grade):
        self.courses[course]=grade
    def get_grades(self):
        return self.courses