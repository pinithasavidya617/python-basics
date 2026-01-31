#Take the principal amount
#interest percentage
#for how many months

principal_amount = int(input("Enter the amount: "))
interest_percentage = float(input("Enter the percentage: "))
years = int(input("For how many years? "))

interest = principal_amount * (interest_percentage / 100) * years
print("LKR",interest)