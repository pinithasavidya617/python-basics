import calculator



def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator: ")

    result = 0

    if  operator == "+":
        result =  calculator.add(num1,num2)
    elif operator == "-":
        result = calculator.sub(num1, num2)
    elif operator == "*":
        result = calculator.multi(num1, num2)
    elif operator == "/":
        result = calculator.multi(num1, num2)
    else:
        print("The operator doesn't exist")


    print(result)

main()

