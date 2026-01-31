import uuid
from typing import Optional

from repository import StudentRepository, CourseRepository, RegistrationRepository
from models import Student, Course, Registration
from dataclasses import dataclass

class StudentCourseError(Exception):
    pass

@dataclass
class StudentManagementService:
    students : StudentRepository
    courses : CourseRepository
    registrations : RegistrationRepository

    def generate_st_id(self):
        return str(uuid.uuid4())[:6]

    def email_validator(self, email:str):
        if "@" not in email:
            raise StudentCourseError("Invalid email! ")
        elif email.startswith("@") or email.endswith("@") or email != email.lower():
            raise StudentCourseError("Invalid email! ")
        else:
            return email

    def add_student(self, name: str, email:str, year:str):
        if self.students.get_by_id(self.generate_st_id()) is not None:
            raise StudentCourseError("This student has been already registered! ")

        self.email_validator(email)

        st_id = self.generate_st_id()
        student = Student(st_id, name, email, year)
        self.students.add(student)
        return student, st_id

    def generate_course_id(self):
        return str(uuid.uuid4()) [:4]

    def add_course(self, title:str, credit: str, lecturer: str):
        if self.courses.get_by_id(self.generate_course_id()) is not None:
            raise StudentCourseError("This course has been already added!")

        course_id = self.generate_course_id()

        course = Course(course_id, title,credit, lecturer)
        self.courses.add(course)
        return course, course_id

    def registration_process(self, st_id: str, course_id:str, semester: str):
       exiting_regs = self.registrations.get_by_student(st_id, semester)
       for r in exiting_regs:
           if r.course_id == course_id:
               raise StudentCourseError(f"Student {st_id} is already enrolled in {course_id} for {semester} semester.")

       total_credits = sum(int(self.courses.get_by_id(r.course_id).credits) for r in exiting_regs)
       new_course = self.courses.get_by_id(course_id)

       if not new_course:
           raise StudentCourseError(f"Course {course_id} does not exists!")

       if total_credits + int(new_course.credits) > 18:
           raise StudentCourseError(
               f"Credit limit exceeded! Current={total_credits}, "
               f"Adding={new_course.credits}, Max=18"
           )

       registration = Registration(st_id, course_id, semester)
       self.registrations.add(registration)
       return registration

    def remove_registration(self, st_id: str, course_id:str, semester: str):
        registration = Registration(st_id, course_id, semester)
        self.registrations.remove(st_id, course_id, semester)
        return registration

    def list_students(self):
        if len(self.students.list_students()) == 0:
            raise StudentCourseError("No students has been registered yet! ")
        return self.students.list_students()

    def list_courses(self):
        if len(self.courses.list_courses()) == 0:
            raise  StudentCourseError("No courses available right now!")
        return self.courses.list_courses()

    def students_transcript(self, st_id:str, semester: Optional[str]):
        if st_id is None:
            raise StudentCourseError("Student id is mandatory!")
        return self.registrations.get_by_student(st_id, semester)

    def course_enrolments(self, course_id:str, semester: Optional[str]):
        if course_id is None:
            raise StudentCourseError("Course id is mandatory!")
        return self.registrations.get_by_course(course_id, semester)

