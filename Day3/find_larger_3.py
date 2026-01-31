#Take two numbers as input and check which one is the largest number
#if num1 > num2 check whether the number is even or odd
#if its an even number check whether its divisible by 4
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2 :
    print(num1 , " >> num1 is the largest number!")
    if num1 % 2 == 0:
        print("It is an even number.")
        if num1 % 4 == 0:
            print("num1 is divisible by 4.")
    else:
        print("It is an odd number.")

elif num2 > num1 :
    print(num2 , " >> num2 is the largest number!")
    if num2 % 2 == 0:
        print("It is an even number.")
        if num2 % 4 == 0 :
            print("num2 is divisible by 4.")
    else:
        print("It is an odd number.")

else:
    print("Both numbers are equal!")
    if num2 % 2 == 0:
        print("Both numbers are even.")
    else:
        print("Both numbers are odd.")




