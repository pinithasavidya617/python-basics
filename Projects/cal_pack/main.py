from calculator import basic, advanced
def get_two_nums():
    num1 = float(input("Enter the number: "))
    num2 = float(input("Enter the number: "))
    return num1, num2

def main():
    print("""
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Power
    6. Square Root
    7. Exit

    """)
    try:
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            num1, num2 = get_two_nums()
            print(f" {num1} + {num2} = {basic.addition(num1, num2)} ")

        elif user_choice == 2:
            num1, num2 = get_two_nums()
            print(f" {num1} - {num2} = {basic.subtract(num1, num2)} ")

        elif user_choice == 3:
            num1, num2 = get_two_nums()
            print(f" {num1} x {num2} = {basic.multiplication(num1, num2)} ")

        elif user_choice == 4:
            try:
                num1, num2 = get_two_nums()
                print(f" {num1} / {num2} = {basic.divide(num1, num2)} ")
            except ZeroDivisionError:
                print("Can't divide by zero! ")

        elif user_choice == 5:
            num1, num2 = get_two_nums()
            print(f" {num1} ^ {num2} = {advanced.power(num1, num2)} ")

        elif user_choice == 6:
            num1 = float(input("Enter the number: "))
            print(f" Square root of {num1} = {advanced.sqrt(num1)}")

        elif user_choice == 7:
            print("Thank you!")

        else:
            print("Enter a valid choice!")

        return user_choice
    except ValueError:
        print("Please enter an integer value!")


while True:
    user_choice = main()
    if user_choice in (7,): break


