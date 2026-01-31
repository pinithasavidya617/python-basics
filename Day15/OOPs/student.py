from dataclasses import dataclass
from typing import List


@dataclass()
class Student:
    student_id : int
    name : str
    age : int
    grades : List[int]


    def add_grades(self, grade) -> None:
        self.grades.append(grade)

    def average(self, grade) -> float:
        if not self.grades:
            return 0.0

        return sum(self.grades) / len(self.grades)


student = Student(1, "Amal", 23, [13])
print(student)

print(student.average([45, 16, 85]))