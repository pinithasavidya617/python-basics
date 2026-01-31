class Student:
    def __init__(self, name, age, campus):
        self.name = name
        self.age = age
        self.institute = campus
        print("Constructor called") #prints once per each object

    def eat(self):
        print(f"Im eating {self.name}, {self.age}")

    def sleep(self):
        print(f"Im sleeping {self.age}")

    def all_properties(self):
        print(f"All: {self.name}, {self.age}, {self.institute}")

    def compare(self, std):
        return self.name == std.name

#Creating an object / instance

student1 = Student("amal", 18, "PO")
student2 = Student("Kamal", 85, "Dead")
student3 = Student("amal", 18, "PO")


student1.eat()
student2.all_properties()
# Student.sleep(student1)
student1.sleep()


print(student1 == student2)
print(student1 == student3)

print(student1)
print(student2)
print(student3)

if student1.compare(student2): #student1 is self here
    print("Students are same")
else:
    print("fk")