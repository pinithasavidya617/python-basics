#Take the first number as an input
# Take the second number as an input
# take the operator which user want to perform
# then check for the operator with if condition and perform the calculation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator ")

#addition
if  operator == "+":
    print("Addition: ", num1 + num2)
elif operator == "-":
    print("Substraction: ", num1 - num2)

elif operator == "*":
    print("Multiplication: ", num1 * num2)

elif operator == "/":
    if num2 == 0:
        print("Can't divide by 0!")
    else:
        print("Divide: ", num1 / num2)

else:
    print("The operator doesn't exist")




