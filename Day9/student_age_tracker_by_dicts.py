details =  {}
def add_student(students ,name, age):
    students[name] = age
    #print(students)
    return students

def view_age(students, name):
    if name in students:
        print( f" {name} -> age is {students[name]}")
    else:
        print("Student not found!")

def remove_data(students, name):
    if name in students:
        del students[name]
        print(f"Student {name} removed.")
    else:
        print("Student not found!")

def main():
    print("""
       1. Add Data
       2. View Age
       3. Delete Data""")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        input_name = input("Enter name: ").lower()
        input_age = int(input("Enter age: "))

        add_student(details, input_name, input_age)
        return choice

    elif choice == 2:
        input_name = input("Enter name: ").lower()
        view_age(details, input_name)
        return choice

    elif choice == 3:
        input_name = input("Enter name: ").lower()
        remove_data(details, input_name)
        return choice

    else:
        print("Invalid choice!")
        return choice


while True:
    choice = main()

    if choice not in (1 , 2, 3): break
