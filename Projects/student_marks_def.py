

marks_list = []


def add_marks(subject_marks_list, subject, marks):
    new_subject = {subject : marks}
    subject_marks_list.append(new_subject)
    print(f"Added {marks} marks for subject: {subject} ")
    return subject_marks_list


def average_marks(subject_marks_list):
    if not subject_marks_list:
        print("No marks available")
        return 0
    else:
        total = 0
        count = 0

        for subject_dictionary in subject_marks_list:
            for subject, marks in subject_dictionary.items():
                total += marks
                count += 1

        if count == 0:
            return 0

        average = total/count
        print(f"Average marks {average:.2f}")
        return average


def grade(average):
    if average >= 75:
        return "Your grade: A"
    elif average >= 50:
        return "Your grade: C"
    elif average >= 35:
        return "Your grade: S"
    else:
        return "You are Fail"


def display_all_marks(subject_marks_list):
    if not subject_marks_list:
        print("Marks list empty")
        return

    for subject_dictionary in subject_marks_list:
        for subject, marks in subject_dictionary.items():
            print(f" Subject {subject} -> {marks} marks.")


def search_subject(subject_marks_list, subject):
    for subject_dictionary in subject_marks_list:
        if subject in subject_dictionary:
            return subject_dictionary[subject]

    return None

def remove_subject(subject_marks_list, subject_name):
    for subject_dictionary in subject_marks_list:
        subject_marks_list.remove(subject_dictionary)
        return f"Subject {subject_name} removed ."
    return None


def main():
    print("""
        === Student Marks Management ===
        1. Add Marks
        2. Calculate Average of Marks
        3. Get Grade from Average
        4. Display All Marks
        5. Search marks
        6. Remove marks
        7. Clear marks
        8. Exit""" )

    choice = int(input("Input your choice: "))

    if choice == 1:
        input_subject = input("Enter subject name: ").lower()
        input_marks = int(input("Enter marks; "))
        add_marks(marks_list, input_subject, input_marks)

    elif choice == 2:
        avg = average_marks(marks_list)

    elif choice == 3:
        avg = average_marks(marks_list)
        student_grade = grade(avg)
        print(student_grade)
    elif choice == 4:
        display_all_marks(marks_list)
    elif choice == 5:
        subject_name = input("Enter subject name: ").lower()
        marks = search_subject(marks_list, subject_name)
        print(f"Subject {subject_name} has {marks} marks.")
    elif choice == 6:
        subject_name = input("Enter subject name to remove: ").lower()
        remove = remove_subject(marks_list, subject_name)
        print(remove)
    elif choice == 7:
        marks_list.clear()
        print("All marks cleared")
    elif choice == 8:
        print("Thank You")
        return False#exit the loop
    else:
        print("Invalid Choice")
while True:
    main()
