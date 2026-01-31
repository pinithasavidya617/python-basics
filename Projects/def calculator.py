import time


def add(x,y):
    return x + y
def substraction(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Can't divide by 0"
    return x / y
while True:
    print("""
    === Calculator === 
    1. Addition
    2. Substraction
    3. Multiplication
    4. divide
    5. Exit """)

    choice = int(input("Choice an option (1-5): "))

    if choice == 5:
        print("Good Bye")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number!")
        continue

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = substraction(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    else:
        print("Invalid option! ")
        continue
    time.sleep(1)
    print("Result: ", result)
