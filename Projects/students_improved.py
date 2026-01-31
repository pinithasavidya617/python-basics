

students = {}
def add_student(student_name):
    if student_name not in students:
        students[student_name] = [] # {john : [] }
        print(f"Student: {student_name} added successfully.")
        return True
    else:
        print(f"Student: {student_name} already exists.")
        return False

def add_marks(student_name, subject, marks):
    if student_name not in students:
        print(f"Student : {student_name} not found!")
        return False

    sub_mark_list = students[student_name] #acess the list, that belongs to student name

    for sub_dict in sub_mark_list:
        if subject in sub_dict:
            sub_dict[subject] = marks
            print(f"Updated marks for student: {student_name}.")
            return True

    new_subject = {subject : marks}
    sub_mark_list.append(new_subject)
    return True


def average_marks(student_name):
    if student_name not in students:
        print(f"Student : {student_name} not found!")
        return None

    sub_marks_list = students[student_name]
    if not sub_marks_list:
        print(f"No available marks for student: {student_name}!")
        return None

    total = 0
    count = 0
    for sub_dict in sub_marks_list:
        for subject, marks in sub_dict.items():
            total += marks
            count += 1

    if count == 0:
        return None

    average = total/count
    print(f" Average : {average:.2f}")
    return average


def get_grade(average):
    if average >= 75:
        return "Grade: A"
    elif average >= 50:
        return "grade: C"
    elif average >= 35:
        return "Grade: S"
    else:
        return "Failed"


# ??????????????
def display_all_marks(student_name = None):
    if student_name:
        if student_name not in students:
            print(f"No marks available for student: {student_name}!")
            return

        sub_marks_list = students[student_name]
        if not sub_marks_list:
            print("No marks available!")
            return

        for sub_dict in sub_marks_list:
            for subject, marks in sub_dict.items():
                print(f"{subject} -> {marks} marks.")
    else:
        if not students:
            print("No students found!")
            return

        print("\nAll Student's Marks")
        for student_name, sub_marks_list in students.items():
            print(f"\nStudent: {student_name}     ")
            if not sub_marks_list:
                print("No marks available")
            else:
                for sub_dict in sub_marks_list:
                    for subject, marks in sub_dict.items():
                        print(f"{subject} -> {marks} marks.")

def search_subject(student_name, subject):
    if student_name not in students:
        print(f"Student: {student_name} not found!")
        return None
    sub_marks_list = students[student_name]

    for sub_dict in sub_marks_list:
        for subject in sub_dict:
            return sub_dict[subject]
    return None


def remove_subject(student_name, subject):
    if student_name not in students:
        print(f"Student: {student_name} not found!")
        return False

    sub_marks_list = students[student_name]

    for sub_dict in sub_marks_list:
        if subject in sub_dict:
            remove = sub_dict[subject]
            sub_marks_list.remove(sub_dict)
            print(f"{subject} subject removed. ({remove} marks.)")
            return True

    print(f"Subject '{subject}' not found")
    return False

def remove_student(student_name):
    if student_name not in students:
        print(f"Student: {student_name} not found!")
        return False

    else:
        del students[student_name]
        print(f"Student: {student_name} removed successfully")
        return True
def list_students():
    if not students:
        print("No students in the list!")
        return

    print("Students in the list:")
    for student_name in students:
        print(student_name)


def main():
    print("""
       === Student Marks Management System ===
       1. Add Student
       2. Add Marks
       3. Calculate Average
       4. Get Grade from Average
       5. Display Marks (specific student)
       6. Display All Students' Marks
       7. Search Marks by Subject
       8. Remove a Subject 
       9. Remove Student
       10. List All Students
       11. Clear All Data
       12. Exit""")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_name = input("Enter student name: ").lower()
        if student_name:
            add_student(student_name)
        else:
            print("Student name cannot be empty!")


    elif choice == 2:
        student_name = input("Enter student name: ").lower()
        if not student_name:
            print("Student name cannot be empty!")

        input_subject = input("Enter the subject: ").lower()
        if not input_subject:
            print("Subject name cannot be empty!")

        input_marks  = int(input("Enter marks: "))
        if 0 <= input_marks <= 100:
            add_marks(student_name, input_subject, input_marks)
        else:
            print("Enter marks between 0 and 100! ")

    elif choice == 3:
        student_name = input("Enter student name: ").lower()
        if student_name:
            avg = average_marks(student_name)
        else:
            print("Student name cannot be empty!")
    elif choice == 4:
        student_name = input("Enter student name: ").lower()
        if student_name:
            avg = average_marks(student_name)
            grade = get_grade(avg)
            print(grade)
        else:
            print("Student name cannot be empty!")

    elif choice == 5:
        student_name = input("Enter student name: ").lower()
        if student_name:
            display_all_marks(student_name)
        else:
            print("Student name cannot be empty!")

    elif choice == 6:
        display_all_marks()

    elif choice == 7:
        student_name = input("Enter student name: ").lower()
        input_subject = input("Enter the subject: ").lower()
        if student_name and input_subject:
            marks = search_subject(student_name, input_subject)
            if marks is not None:
                print(f"{input_subject} has {marks} marks.")
            else:
                print(f"Marks of {input_subject} not found.")
        else:
            print("Student name and subject are required!")

    elif choice == 8:
        student_name = input("Enter student name: ").lower()
        input_subject = input("Enter the subject to remove: ").lower()
        if student_name and input_subject:
            removed = remove_subject(student_name, input_subject)
        else:
            print("Student name and subject are required!")

    elif choice == 9:
        student_name = input("Enter student name: ").lower()
        if student_name:
            remove_student(student_name)
        else:
            print("Student name cannot be empty!")

    elif choice == 10:
        list_students()

    elif choice == 11:
        print("Clearing the list...")
        students.clear()

    elif choice == 8:
        print("Thank you")
        return False
    else:
        print("Invalid choice!")

    return True


while True:
    main()
    pass




