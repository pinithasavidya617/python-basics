from typing import List


class Student:
    def __init__(self, student_id: str, name: str, age: int, grades:List[int]):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = grades

    def __eq__(self, obj2): #overriding equal method in object class
        return self.name == obj2.name

    def add_grades(self, grade) -> None: #returning None
        self.grades.append(grade)

    def average(self, grade) -> float: #returning float
        if not self.grades:
            return 0.0

        return sum(self.grades) / len(self.grades)

    def get_student_info(self):
        return self.student_id, self.name, self.age, self.grades

student = Student("a15", "aaa", 45, [15, 17])
student2 = Student("a15", "aaa", 45, [15, 17])

print(student.average([15, 17, 28]))

if student == student2: #false if __eq not defined
    print("YES")

