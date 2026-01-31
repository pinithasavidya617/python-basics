def add(first_num,second_num):
    return first_num + second_num
def sub(first_num,second_num):
    return first_num - second_num
def multi(first_num,second_num):
    return  first_num * second_num
def divide(first_num,second_num):
    if second_num == 0:
        return "Can't divide by 0!"
    else:
        return first_num/second_num

pi = 3.14
def calculate_circle_diameter(radius):
    diameter = 2 * pi * radius
    return diameter

#print(__name__)

if __name__ == "__main__":    #Uses for test cases. This will not be printed in "main" file or others. It will be printed only in this file.
    print(__name__)
    print(add(45, 55))
    print(calculate_circle_diameter(7))