from abc import ABC, abstractmethod
from typing import List, Optional, Dict

from models import Student, Course, Registration

class StudentRepository(ABC):
    @abstractmethod
    def add(self, student : Student) -> None:
        pass

    @abstractmethod
    def get_by_id(self, student_id : str)-> Student:
        pass

    @abstractmethod
    def update(self, student : Student)-> None:
        pass

    @abstractmethod
    def list_students(self) -> List:
        pass

class CourseRepository(ABC):
    @abstractmethod
    def add(self, course: Course) -> None:
        pass

    @abstractmethod
    def get_by_id(self, course_id: str) -> Course:
        pass

    @abstractmethod
    def update(self, course: Course) -> None:
        pass

    @abstractmethod
    def list_courses(self) -> List:
        pass

class RegistrationRepository(ABC):
    @abstractmethod
    def add(self, registration : Registration)-> None:
        pass

    @abstractmethod
    def remove(self, student_id: str, course_id: str, semester: str):
        pass

    @abstractmethod
    def get_by_student(self, student_id:str, semester: Optional[str]) -> List[Registration]:
        pass

    @abstractmethod
    def get_by_course(self, course_id, semester: Optional[str]) -> List[Registration]:
        pass

    def list_all(self) -> List[Registration]:
        pass

class FileStudentRepository(StudentRepository):
    def __init__(self, filename:str = "students.txt"):
        self.filename = filename

    def save_student(self,students: Dict[str, Student]):
        with open(self.filename, "w") as f:
            for student in students.values():
                f.write(f"{student.st_id}|{student.name}|{student.email}|{student.year}\n")

    def load_student(self):
        students = {}
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    line = line.strip()
                    data = line.split("|")
                    if len(data) == 4:
                        st_id, name, email, year = data
                        students[st_id] = Student(st_id, name, email, year)

        except FileNotFoundError:
            pass
        return students

    def add(self, student: Student) -> None:
        students : Dict[str, Student] = self.load_student()
        students[student.st_id] = student
        self.save_student(students)

    def get_by_id(self, student_id: str) -> Student:
        students = self.load_student()
        return students.get(student_id)

    def update(self, student: Student) -> None:
        students: Dict[str, Student] = self.load_student()
        students[student.st_id] = student
        self.save_student(students)

    def list_students(self) -> List:
        students = self.load_student()
        return list(students.values())

class FileCourseRepository(CourseRepository):


    def __init__(self, filename:str = "course.txt"):
        self.filename = filename

    def save_course(self, courses: Dict[str, Course]):
        with open (self.filename, "w") as f:
            for course in courses.values():
                f.write(f"{course.course_id}|{course.title}|{course.credits}|{course.lecturer}\n")

    def load_course(self):
        courses = {}
        try:
            with open(self.filename, "r")as f:
                for line in f:
                    line = line.strip()
                    data = line.split("|")
                    if len(data) == 4:
                        course_id, title, credit, lecturer = data
                        courses[course_id] = Course(course_id, title, credit, lecturer)
        except FileNotFoundError:
            pass
        return courses

    def add(self, course: Course) -> None:
        courses : Dict[str, Course] = self.load_course()
        courses[course.course_id] = course
        self.save_course(courses)

    def get_by_id(self, course_id: str) -> Course:
        courses = self.load_course()
        return courses.get(course_id)

    def update(self, course: Course) -> None:
        courses: Dict[str, Course] = self.load_course()
        courses[course.course_id] = course
        self.save_course(courses)

    def list_courses(self) -> List:
        courses = self.load_course()
        return list(courses.values())


class FileRegistrationRepository(RegistrationRepository):
    def __init__(self, filename: str = "registration.txt"):
        self.filename = filename

    def save_registration(self, registrations: Dict[str, Registration]):
        with open(self.filename, "w")as f:
            for registration in registrations.values():
                f.write(f"{registration.st_id}|{registration.course_id}|{registration.semester}\n")

    def load_registration(self):
        registrations = {}
        try:
            with open(self.filename, "r")as f:
                for line in f:
                    line = line.strip()
                    data = line.split("|")
                    if len(data) == 3:
                        st_id, course_id, semester = data
                        key = f"{st_id}_{course_id}_{semester}" #Composite key
                        registrations[key] = Registration(st_id, course_id, semester)

        except FileNotFoundError:
            pass
        return registrations

    def add(self, registration: Registration) -> None:
        registrations : Dict[str, Registration] = self.load_registration()
        key = f"{registration.st_id}_{registration.course_id}_{registration.semester}"
        registrations[key] = registration
        self.save_registration(registrations)

    def remove(self, student_id: str, course_id: str, semester: str):
        registrations = self.load_registration()
        key = f"{student_id}_{course_id}_{semester}"
        if key in registrations:
            del registrations[key]
        self.save_registration(registrations)

    def get_by_student(self, student_id: str, semester: Optional[str]) -> List[Registration]:
        registrations = self.load_registration()
        result = [
            r for r in registrations.values()
            if r.st_id == student_id and  (semester is None or r.semester == semester)
        ]
        return result

    def get_by_course(self, course_id, semester: Optional[str]) -> List[Registration]:
        registrations = self.load_registration()
        result = [
            r for r in registrations.values()
            if r.course_id == course_id and (semester is None or r.semester == semester)
        ]
        return  result

