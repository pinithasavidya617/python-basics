
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


def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator: ")

    result = 0

    if  operator == "+":
        result =  add(num1, num2)
    elif operator == "-":
        result = sub(num1, num2)
    elif operator == "*":
        result = multi(num1, num2)
    elif operator == "/":
        result = divide(num1,num2)
    else:
        print("The operator doesn't exist")


    print(result)

main()




