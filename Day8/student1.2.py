
marks_list = []


def add_marks(sub_mark_list, subject, marks):
    for sub_dict in sub_mark_list:
        if subject in sub_dict:
            sub_dict[subject] = marks
            return sub_mark_list

    new_subject = {subject : marks}
    sub_mark_list.append(new_subject)
    return sub_mark_list


def average_marks(sub_marks_list):
    if not sub_marks_list:
        print("No available marks for calculate the average!")
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
        return "Your grade: A"
    elif average >= 50:
        return "Your grade: C"
    elif average >= 35:
        return "Your grade: S"
    else:
        return "You are Fail"


def display_all_marks(sub_marks_list):
    if not sub_marks_list:
        print("No marks available!")
        return

    for sub_dict in sub_marks_list:
        for subject, marks in sub_dict.items():
            print(f"{subject} -> {marks} marks.")


def search_subject(sub_marks_list, subject):
    for sub_dict in sub_marks_list:
        for subject in sub_dict:
            return sub_dict[subject]
    return None


def remove_subject(sub_marks_list, subject):
    for sub_dict in sub_marks_list:
        if subject in sub_dict:
            remove = sub_dict[subject]
            sub_marks_list.remove(sub_dict)
            print(f"{subject} subject removed. ({remove} marks.)")
            return True
    print(f"Subject '{subject}' not found")
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

    choice = int(input("Enter your choice: "))

    if choice == 1:
        input_subject = input("Enter the subject: ").lower()
        input_marks  = int(input("Enter marks: "))
        if 0 <= input_marks <= 100:
            add_marks(marks_list, input_subject, input_marks)
        else:
            print("Enter marks between 0 and 100! ")
    elif choice == 2:
        avg = average_marks(marks_list)
    elif choice == 3:
        avg = average_marks(marks_list)
        grade = get_grade(avg)
        print(grade)
    elif choice == 4:
        display_all_marks(marks_list)
    elif choice == 5:
        input_subject = input("Enter the subject: ").lower()
        marks = search_subject(marks_list, input_subject)
        if marks is not None:
            print(f"{input_subject} has {marks} marks.")
        else:
            print(f"Marks of {input_subject} not found.")
    elif choice == 6:
        input_subject = input("Enter the subject to remove: ").lower()
        removed = remove_subject(marks_list, input_subject)
    elif choice == 7:
        print("Clearing the list...")
        marks_list.clear()
    elif choice == 8:
        print("Thank you")
        return False
    else:
        print("Invalid choice!")

while True:
    main()
    pass




