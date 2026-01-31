#When user gives the birth year ,you should print his age
birthyear = int(input("Enter your birth year: "))#Must call int( )because input came like a string at default
this_year = int(input("Enter current year: "))
age = this_year - birthyear
print("Age: ", age)