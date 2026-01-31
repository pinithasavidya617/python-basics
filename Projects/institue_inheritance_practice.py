class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"{self.name} is {self.age} years old."

class Staff(Person):
    def __init__(self, name, age, department):
        Person.__init__(self,name,age)
        self.department = department

    def work(self):
        return f"{self.name} works in {self.department} department."

class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(self,name,age)
        self.grade = grade

    def study(self):
        return f"{self.name} is studying at grade {self.grade}."

class Teacher(Staff):
    def __init__(self, name, age, department, subject):
        Staff.__init__(self,name,age,department)
        self.subject = subject

    def teach(self):
        return f"{self.name} teaches {self.subject}."

class Admin(Staff):
    def __init__(self, name, age, department, role):
        Staff.__init__(self,name,age,department)
        self.role = role

    def duty(self):
        return f"{self.name} does {self.role} role at {self.department}."

class Undergraduate(Student):
    def __init__(self,name, age, grade, major):
        Student.__init__(self, name, age, grade)
        self.major = major

    def project(self):
        return f"{self.name} is doing {self.major}."

class Graduate(Student):
    def __init__(self,name, age, grade, thesis_title):
        Student.__init__(self, name, age, grade)
        self.thesis_title = thesis_title

    def research(self):
        return f"{self.name} did {self.thesis_title} as the research."



teacher = Teacher("Alice", 35, "Science", "Physics")
print(teacher.introduce())
print(teacher.work())
print(teacher.teach())

print("-------------")

ug_student = Undergraduate("Bob", 20, "Year 2", "Computer Science")
print(ug_student.introduce())
print(ug_student.study())
print(ug_student.project())

print("-------------")

grad_student = Graduate("Clara", 26, "Year 5", "AI in Education")
print(grad_student.introduce())
print(grad_student.study())
print(grad_student.research())





