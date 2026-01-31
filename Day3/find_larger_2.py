#Take two numbers as input and check which one is the largest number
#if num1 > num2 check whether the number is even or odd
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2 :
    print(num1 , " >> num1 is the largest number!")
    if num1 % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
elif num2 > num1 :
    print(num2 , " >> num2 is the largest number!")
    if num2 % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
else:
    print("Both numbers are equal!")
    if num2 % 2 == 0:
        print("Both numbers are even.")
    else:
        print("Both numbers are odd.")




