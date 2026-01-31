import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional



@dataclass
class Student:
    first_name : str
    last_name : str
    address : str
    nic : str
    nationality : str
    academic_year : str
    st_id : Optional[str] = None

    def __post_init__(self):
        if self.st_id is None:
            self.st_id =  f"ST-{str(uuid.uuid4()) [:8].upper()}"

    def get_student_info(self):
        return f" Student ID: {self.st_id} | Name: {self.first_name} {self.last_name}"

    def get_age(self):
        birth_year = 0
        nic_for_age = self.nic.strip().upper()
        if len(nic_for_age) == 12:
            birth_year = int(nic_for_age[0:4])
        elif len(nic_for_age) == 10 and nic_for_age[-1] in ("V", "X"):
            birth_year = 1900 + int(nic_for_age[0:2])
        else:
            "Invalid NIC!"

        current_year = datetime.now().year
        age = current_year - birth_year
        return f"{self.first_name}'s age: {age}"

    def get_gender(self):
        nic_for_gender = self.nic.strip().upper()
        if len(nic_for_gender) == 12:
            day_of_year = int(self.nic[4:7])
        elif len(nic_for_gender) == 10 and nic_for_gender[-1] in ("V" , "X"):
            day_of_year = int(nic_for_gender[2:5])
        else:
            return "Invalid NIC!"

        if day_of_year > 500:
            return f"{self.first_name} is Female"
        else:
            return f"{self.first_name} is Male"

    def get_birthday(self):
        nic_for_birthday = self.nic.strip().upper()

        if len(nic_for_birthday) == 12:
            birth_year = int(nic_for_birthday[0:4])
            day_of_year = int(nic_for_birthday[4:7])
            if day_of_year >= 59:
                day_of_year -= 1

        elif len(nic_for_birthday) == 10 and nic_for_birthday[-1] in ("V", "X"):
            birth_year = 1900 + int(nic_for_birthday[0:2])
            day_of_year = int(nic_for_birthday[2:5])
            day_of_year -= 1
        else:
            return "Invalid NIC"

        try:
            if day_of_year > 500:
                day_of_year -= 500

            if not (1 <= day_of_year <= 366):
                return "Invalid NIC"

            date_str = f"{birth_year}{day_of_year:03d}"
            birthday = datetime.strptime(date_str, "%Y%j")
            return birthday.strftime(f"{self.first_name}'s birthday : %Y-%m-%d")
        except ValueError:
            return "Invalid NIC!"

def is_nic_duplicate(students_list : List[Student], nic: str):
    for st in students_list:
        if st.nic.strip().upper() == nic.strip().upper():
            return True
    return False

def find_student_by_id(student_list : List[Student], student_id: str):
    for st in student_list:
        if st.st_id == student_id:
            return st
    return None

def display_all_students(student_list : List[Student]):
    if not student_list:
        print("No students found!")
        return

    for st in student_list:
        print(st.get_student_info())

def find_student_by_nic(student_list : List[Student], nic: str):
    for st in student_list:
        if st.nic.strip().upper() == nic.strip().upper():
            return st
    return None

def get_by_academic_year(student_list, year):
    academic_by_list = [st for st in student_list if st.academic_year == year]
    if not academic_by_list:
        return None
    for std in academic_by_list:
        print(f"Name: {std.first_name} {std.last_name} |NIC: {std.nic}| Address: {std.address} | Nationality: {std.nationality} ")
    return None


def get_by_nationality(student_list, nation):
    nationality_by_list = [st for st in student_list if st.nationality.lower() == nation.lower()]
    if not nationality_by_list:
        return None
    for std in nationality_by_list:
        print(f"Name: {std.first_name} {std.last_name} |NIC: {std.nic} | Address: {std.address} | Academic Year: {std.academic_year} ")
    return None

def save_students(students_list : List[Student], filename: str = "students.txt"):
    try:
        with open(filename, "w") as f:
            for st in students_list:
                f.write(f"{st.st_id}|{st.first_name}|{st.last_name}|{st.nic}|{st.address}|{st.academic_year}|{st.nationality}\n")
        print(f"Successfully saved {len(students_list)} students!")

    except Exception as e:
        print(f"Error saving file: {e}")



def load_students(filename:str = "students.txt"):
    students_list = []
    try:
        with open(filename, "r")as f:
            for line in f:
                line = line.strip()
                data = line.split("|")
                if len(data) == 7:
                    st_id, first_name, last_name, nic, address, academic_year, nationality = data
                    students_list.append(Student(first_name=first_name,
                                                 last_name=last_name,
                                                 address=address,
                                                 nic=nic,
                                                 nationality=nationality,
                                                 academic_year=academic_year,
                                                 st_id=st_id))
        return students_list

    except FileNotFoundError as e:
        print(e)
        return []

    except Exception as e:
        print(f"Error loading file: {e}")
        return []


students: List[Student] = load_students()

print("=" * 15, "STUDENT MANAGEMENT SYSTEM", "=" * 15)
while True:
    print("""
        1. Add a New Student
        2. Get Student ID
        3. Get Student Gender
        4. Get Student Birthday
        5. Get Age
        6. Get Students by Academic Year
        7. Get Students by Nationality
        0. Exit
    """)
    try:
        choice = int(input("-> \tEnter your choice: "))
        if choice == 1:
            first_name = input("Enter first name: ").capitalize()
            last_name = input("Enter last name: ").capitalize()
            address = input("Enter address: ").capitalize()
            while True:
                nic = input("Enter NIC: ")
                if not nic:
                    print("NIC cannot be empty!")
                    continue

                if is_nic_duplicate(students, nic):
                    exiting_student = find_student_by_nic(students, nic)
                    if exiting_student:
                        print("This NIC number already exists in system!")
                        print(f"{exiting_student.first_name} has been registered already with this NIC,")
                        print("Please try another NIC!")
                        continue

                valid_nic = nic.strip().upper()
                if len(valid_nic) == 12 and valid_nic.isdigit():
                    break
                elif len(valid_nic) == 10 and valid_nic[-1] in ("V", "X"):
                    break
                else:
                    print("Invalid NIC format!")
                    continue

            nationality =  input("Enter nationality: ").capitalize()
            academic_year = input("Enter academic year: ")

            student = Student(first_name, last_name, address, nic, nationality, academic_year)
            students.append(student)
            print("New student added successfully!")
            save_students(students)

        elif choice == 2:
            display_all_students(students)

        elif choice == 3:
            if not students:
                print("No students found!")
            else:
                display_all_students(students)
                student_id = input("Enter Student ID: ").strip()

                student = find_student_by_id(students, student_id)
                if student:
                    print(student.get_gender())
                else:
                    print("Student not found!")

        elif choice == 4:
            if not students:
                print("No students found!")
            else:
                display_all_students(students)
                student_id = input("Enter Student ID: ").strip()
                student = find_student_by_id(students, student_id)
                if student:
                    print(student.get_birthday())
                else:
                    print("Student not found!")

        elif choice == 5:
            if not students:
                print("No students found!")
            else:
                display_all_students(students)
                student_id = input("Enter Student ID: ").strip()
                student = find_student_by_id(students, student_id)
                if student:
                    print(student.get_age())
                else:
                    print("Student not found!")

        elif choice == 6:
            if not students:
                print("No students found!")
            else:
                year = input("Enter academic year: ")
                get_by_academic_year(students, year)

        elif choice == 7:
            if not students:
                print("No students found!")
            else:
                nation = input("Enter nationality: ")
                get_by_nationality(students, nation)

        elif choice == 0:
            save_students(students)
            print("Thank you for using Student Management System!")
            break
        else:
            print("Enter a valid number!")
            continue
    except ValueError:
        print("Enter a valid number!")
        continue
