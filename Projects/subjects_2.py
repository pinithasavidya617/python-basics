marks_list = []


def add_marks(subject_marks_list, subject, marks):

    for subject_dic in subject_marks_list:
        if subject in subject_dic:
            subject_dic[subject] = marks
            return subject_marks_list

    new_subject = {subject : marks}
    subject_marks_list.append(new_subject)
    print(f"Subject: {subject} added successfully.")
    return subject_marks_list


def average_of_marks(subjects_marks_list):
    if not subjects_marks_list:
        print("No marks available")
        return 0

    total = 0
    count = 0
    for subject_dic in subjects_marks_list:
        for subject, marks in subject_dic.items():
            total += marks
            count += 1
    if count == 0:
        return 0

    average = total/count
    print(f"Average : {average:.2f}")
    return average


def get_grade(average):
    if average >= 75:
        return "Your grade: A"
    elif average >= 50:
        return "Your grade: C"
    elif average >= 35:
        return "Your grade: S"
    else:
        return "You are Fail"


def display_grade(subjects_marks_list):
    if not subjects_marks_list:
        print("No marks available")
        return

    for subject_dic in subjects_marks_list:
        for subject, marks in subject_dic.items():
            print(f" Subject: {subject.capitalize()} --> {marks} marks.")


def search_subject(subjects_marks_list, subject):
    for subject_dic in subjects_marks_list:
        if subject in subject_dic:
            return subject_dic[subject]
    return None


def remove_subject(subjects_marks_list, subject):
    for subject_dic in subjects_marks_list:
        if subject in subject_dic:
            removed_marks = subject_dic[subject]
            subjects_marks_list.remove(subject_dic)
            print(f"Removed {subject} (marks: {removed_marks})")
            return True
    print(f"Subject '{subject} not found")
    return False

def main():
    print("""
    1. Add Marks
    2. Average of Marks
    3. Get Grade from Average
    4. Display Marks
    5. Search Marks from Subject
    6. Remove a Subject 
    7. Clear the List
    8. Exit""")
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            input_subject = input("Enter the subject name: ").lower()
            input_marks = int(input("Enter the marks: "))
            if 0 <= input_marks <= 100:
                add_marks(marks_list, input_subject, input_marks)
            else:
                print("Please enter marks between 0 and 100")

        elif choice == 2:
            avg = average_of_marks(marks_list)

        elif choice == 3:
            if marks_list:
                avg = average_of_marks(marks_list)
                grade = get_grade(avg)
                print(grade)
            else:
                print("No marks available")

        elif choice == 4:
            display_grade(marks_list)

        elif choice == 5:
            input_subject = input("Enter the subject: ").lower()
            marks = search_subject(marks_list, input_subject)
            if marks is not None:
                print(f"{input_subject} has {marks} marks.")
            else:
                print(f'Subject {input_subject} not found.')

        elif choice == 6:
            input_subject = input("Enter the subject: ").lower()
            remove_subject(marks_list, input_subject)

        elif choice == 7:
            print("List cleared successfully")
            marks_list.clear()

        elif choice == 8:
            print("Thank You")
            return False

        else:
            print("Invalid Choice(Choose 1-8)")
    except ValueError:
        print("Please enter a valid number.")
    return True

while main():
    pass
