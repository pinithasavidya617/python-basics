

# student grading system
# take marks of upto 5 subjects
# then calculate the avarage of marks
# based on the average grade the student
# less than 35 fail
# more than 50 C
# more than 75 A
marks = []
for i in range(5):
    user_marks = int(input("Enter the marks: "))
    marks.append(user_marks)

average = sum(marks) / len(marks)
print(f"Average :{average}")
max_marks = max(marks)
print(f"The highest score is {max_marks}")

if average > 75:
    print("Your grade: A")
elif average > 50:
    print("Your grade: C")
elif average > 35:
    print("Your grade: S")
elif average < 35:
    print("You are Fail")


