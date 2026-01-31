marks_list = []


def add_marks(subject_marks_list, subject, marks):
    """
    Returns: subject_marks_list (the modified list)
    Why: To allow chaining operations or to confirm the list was updated
    """
    for subject_dic in subject_marks_list:
        if subject in subject_dic:
            subject_dic[subject] = marks
            print(f"Subject: {subject} updated successfully.")
            return subject_marks_list  # Return the updated list

    new_subject = {subject: marks}
    subject_marks_list.append(new_subject)
    print(f"Subject: {subject} added successfully.")
    return subject_marks_list  # Return the updated list


def average_of_marks(subjects_marks_list):
    """
    Returns: 0 (number) if no marks, average (number) if marks exist
    Why: 0 indicates "no data", actual number is the calculated average
    """
    if not subjects_marks_list:
        print("No marks available")
        return 0  # Return 0 to indicate no marks available

    total = 0
    count = 0
    for subject_dic in subjects_marks_list:
        for subject, marks in subject_dic.items():
            total += marks
            count += 1
    if count == 0:
        return 0  # Return 0 if somehow no marks were found

    average = total / count
    print(f"Average : {average:.2f}")
    return average  # Return the calculated average number


def get_grade(average):
    """
    Returns: String (grade message)
    Why: Returns a text message to display to user
    """
    if average >= 75:
        return "Your grade: A"  # Return string message
    elif average >= 50:
        return "Your grade: C"  # Return string message
    elif average >= 35:
        return "Your grade: S"  # Return string message
    else:
        return "You are Fail"  # Return string message


def display_grade(subjects_marks_list):
    """
    Returns: None (nothing)
    Why: This function only prints, doesn't need to return anything
    """
    if not subjects_marks_list:
        print("No marks available")
        return  # Return nothing (None) - just exit function early

    for subject_dic in subjects_marks_list:
        for subject, marks in subject_dic.items():
            print(f" Subject: {subject.capitalize()} --> {marks} marks.")
    # No return statement = returns None automatically


def search_subject(subjects_marks_list, subject):
    """
    Returns: None if not found, marks (number) if found
    Why: None indicates "not found", number indicates "found with this value"
    """
    for subject_dic in subjects_marks_list:
        if subject in subject_dic:
            return subject_dic[subject]  # Return the marks (number)
    return None  # Return None to indicate "not found"


def remove_subject(subjects_marks_list, subject):
    """
    Returns: True if removed successfully, False if not found
    Why: True/False clearly indicates success or failure
    """
    for subject_dic in subjects_marks_list:
        if subject in subject_dic:
            removed_marks = subject_dic[subject]
            subjects_marks_list.remove(subject_dic)
            print(f"Removed {subject} (marks: {removed_marks})")
            return True  # Return True to indicate "success"
    print(f"Subject '{subject}' not found")
    return False  # Return False to indicate "failed/not found"


def main():
    """
    Returns: True to continue program, False to exit program
    Why: Controls whether the while loop should continue or stop
    """
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
            if marks is not None:  # Check if None (not found)
                print(f"{input_subject} has {marks} marks.")
            else:
                print(f'Subject {input_subject} not found.')

        elif choice == 6:
            input_subject = input("Enter the subject: ").lower()
            success = remove_subject(marks_list, input_subject)
            # Could use the True/False return value if needed
            # if success:
            #     print("Removal successful!")

        elif choice == 7:
            print("List cleared successfully")
            marks_list.clear()

        elif choice == 8:
            print("Thank You")
            return False  # Return False to indicate "exit program"

        else:
            print("Invalid Choice(Choose 1-8)")
    except ValueError:
        print("Please enter a valid number.")

    return True  # Return True to indicate "continue program"


# FIXED: Check the return value from main()
while main():  # This will stop when main() returns False
    print("-" * 40)  # Visual separator

print("Program ended.")

# Alternative way to write the same thing:
# running = True
# while running:
#     running = main()  # running becomes False when user chooses exit
#     if running:
#         print("-" * 40)