details = {}


def add_student(students, student_id, name, age, address, contact):
    students[student_id] = {
        "name": name,
        "age": age,
        "address": address,
        "contact": contact

    }
    # print(students)
    return students


def view_age(students, student_id):
    if student_id in students:
        print(f"Student : {student_id} - {students[student_id]}")
    else:
        print(f"Student id {student_id} not found!")


def remove_data(students, student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student id {student_id} removed.")
    else:
        print(f"Student id {student_id} not found!")


def update_contact(students, student_id, updated_contact):
    if student_id in students:
        students[student_id]['contact'] = updated_contact
        print(f"Updated list: {students[student_id]}")

    else:
        print(f"Student id {student_id} not found!")


def view_names(students):
    for st_id in students.keys():
        print(f"{st_id} : {students[st_id]['name']}")


# def view_names(students):
#     for key, val in students.items():
#         print(f"{key} - {val['name']}")

def add_marks(student_id, students):
    if student_id in students:
        try:
            maths = int(input("Enter marks of Maths: "))
            science = int(input("Enter marks of Science: "))
            english = int(input("Enter marks of English: "))

            students[student_id]["marks"] = {
                'maths': maths,
                'science': science,
                'english': english
            }

            print("Marks added successfully")

        except ValueError:
            print("You can only add integer values")
            add_marks(student_id, students)


    else:
        print(f"Student id {student_id} not found!")


def view_marks(student_id, students):
    if student_id in students:
        if "marks" in students[student_id]:
            print(f"Marks for student: {students[student_id]['name']}")

            for key,val in students[student_id]["marks"].items():
                print(f"Subject - {key} | Marks - {val}")
        else:
            print("Marks not available for this student")
    else:
        print(f"Student id {student_id} not found!")

def average_of_marks(student_id, students):
    if student_id in students:
        for key, val in students.items(): #key = st_id
            if "marks" in val:
                total = 0

                for mark in val["marks"].values():
                    total += mark

                print(f"{val['name']} average : {total//3}")

                print(f"Your grade is {get_grade(total//3)}")

    else:
        print(f"Student id {student_id} not found!")

def get_grade(grade):
    if grade >= 75:
        return "A"
    elif grade >= 60:
        return "B"
    elif grade >= 60:
        return "C"
    elif grade >= 35:
        return "S"
    else:
        return "F"

def main():
    print("""
       1. Add Data
       2. View Details
       3. Delete Data
       4. Update Contact Number
       5. View All Names
       6. Add Marks
       7. View Marks
       8. Average of Marks
       """)
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            st_id = input("Enter Student id: ")
            input_name = input("Enter name: ").lower()
            input_age = int(input("Enter age: "))
            input_address = input("Enter address: ").lower()
            input_phone = input("Enter phone number: ")

            add_student(details, st_id, input_name, input_age, input_address, input_phone)
            return choice

        elif choice == 2:
            st_id = input("Enter Student id: ")
            view_age(details, st_id)
            return choice

        elif choice == 3:
            st_id = input("Enter Student id: ")
            remove_data(details, st_id)
            return choice

        elif choice == 4:
            st_id = input("Enter Student id: ")
            input_phone_updated = input("Enter phone number: ")
            update_contact(details, st_id, input_phone_updated)
            return choice

        elif choice == 5:
            view_names(details)
            return choice

        elif choice == 6:
            st_id = input("Enter Student id: ")

            add_marks( st_id, details)

            return choice
        elif choice == 7:
            st_id = input("Enter Student id: ")
            view_marks(st_id, details)
            return choice

        elif choice == 8:
            st_id = input("Enter Student id: ")
            average_of_marks(st_id, details)
            return choice


        else:
            print("Invalid choice!")
            return choice
    except ValueError:
        print("Please enter an integer value")

while True:
    choice = main()

    if choice not in (1, 2, 3, 4, 5, 6, 7, 8): break
