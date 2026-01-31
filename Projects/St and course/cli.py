from repository import FileCourseRepository, FileStudentRepository, FileRegistrationRepository
from service import StudentCourseError, StudentManagementService
student_management = StudentManagementService(students=FileStudentRepository(),
                                              courses=FileCourseRepository(),
                                              registrations=FileRegistrationRepository())

def add_student():
    name = input("Enter student name: ")
    email = input("Enter email: ")
    year = input("Enter academic year: ")
    try:
        student, st_id = student_management.add_student(name, email, year) # return student, st_id in service layer
        print(f"Student: {name} added successfully!, Student id is {st_id}")
    except StudentCourseError as e:
        print(e)


def add_course():
    title = input("Enter course title: ")
    credit = input("Enter credit value of the course: ")
    lecturer = input("Enter the lecturer name: ")
    try:
        course, course_id = student_management.add_course(title, credit, lecturer)
        print(f"Course: {title} added successfully!, Course id is {course_id} ")
    except StudentCourseError as e:
        print(e)

def registration_process():
    st_id = input("Enter student id: ")
    course_id = input("enter course id: ")
    semester = input("Enter the semester: ")
    try:
        student_management.registration_process(st_id, course_id, semester)
        print(f"Registration successful for student id: {st_id} in course {course_id} for {semester} semester.")
    except StudentCourseError as e:
        print(e)

def drop_course():
    st_id = input("Enter student id: ")
    course_id = input("enter course id: ")
    semester = input("Enter the semester: ")
    try:
        student_management.remove_registration(st_id, course_id, semester)
        print(f"course id {course_id} dropped from student id {st_id}!")
    except StudentCourseError as e:
        print(e)

def student_transcript():
    st_id = input("Enter student id: ")
    semester = input("Enter the semester: ")
    try:
        print( student_management.students_transcript(st_id, semester))
    except StudentCourseError as e:
        print(e)

def course_enrolments():
    course_id = input("enter course id: ")
    semester = input("Enter the semester: ")
    try:
        print(student_management.course_enrolments(course_id, semester))
    except StudentCourseError as e:
        print(e)

while True:
    print("""
1. Add student
2. Add course
3. Enrol student in course
4. Drop course
5. View student transcript
6. View course enrolments
0. Exit
""")
    try:
        choice = int(input("ENTER YOUR CHOICE: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            add_course()
        elif choice == 3:
            registration_process()
        elif choice == 4:
            drop_course()
        elif choice == 5:
            student_transcript()
        elif choice == 6:
            course_enrolments()
        elif choice == 0:
            break
        else:
            print("Enter a valid choice!")

    except ValueError:
        print("Enter a valid choice!")