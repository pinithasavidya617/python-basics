from typing import List

student_names = ["kalana", "pasan", "dasun"]#iterable

# print(help(student_names))
print(type(student_names))
student_iterator = student_names.__iter__() #calling dunder method to get an iterator

for student in student_names:
    print(student)
print()

try:
    print(student_iterator.__next__())  #backend of a for loop
    print(student_iterator.__next__())
    print(student_iterator.__next__())
    print(student_iterator.__next__())

except StopIteration as e:
    print(e)

print()


student_iterator2 = iter(student_names)

print(next(student_iterator2))
print(next(student_iterator2))


class CountDown: #implementing iterator protocol
    def __init__(self, num: int):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        self.num -= 1
        if self.num == 0:
            raise StopIteration
        return self.num

count_down = CountDown(10)
count_down_itr = iter(count_down)

print(count_down_itr.__next__())
print(count_down_itr.__next__())
print(count_down_itr.__next__())

print("+++++++++++++++++++++++++++++++")


for i in count_down:
    print(i)

print("++++++++++")

def generate_numbers(n: int) -> List[int]:
    result = []

    for i in range(n):
        result.append(i)
    return result

for num in generate_numbers(10):
    print(num)