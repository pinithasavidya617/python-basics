def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be less than zero") #Raising exceptions in a function
    else:
        print(age)
check_age(-1)
# try:
#     check_age(-1)
# except ValueError:
#     print("Value error occurred")