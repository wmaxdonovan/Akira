from abc import ABC
from .course_base import Course


class Semester:
    def __init__(self, data):
        self.year = data['year']
        self.semester = data['semester']
        self.courses = {}
        for course in data['courses']:
            self.courses[course] = Course(data[course])
