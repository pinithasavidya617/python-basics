
monthly_salary = float(input("Enter your monthly salary: "))
annual_salary = monthly_salary * 12
if annual_salary <= 1200000 :
    print("You have no tax")
else:
    taxable_income = annual_salary - 1200000

    if(taxable_income <= 500000):
        tax = (taxable_income * 0.06)
    elif(taxable_income <= 1000000):
        tax = ((500000 * 0.06) + (taxable_income - 500000) * 0.12)
    elif(taxable_income <= 1500000):
        tax = ((500000 * 0.06) + (500000 * 0.12) + (taxable_income - 1000000) * 0.18)
    elif(taxable_income <= 2000000) :
        tax = ((500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (taxable_income - 1500000) * 0.24)
    elif(taxable_income <= 2500000) :
        tax = ((500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + (taxable_income - 2000000) * 0.30)
    else:
        tax = ((500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + (500000 * 0.30) + (taxable_income - 2500000) * 0.36)

    print(f"Your monthly tax is LKR {tax / 12} ")
    print(f"take home salary: LKR {monthly_salary - (tax/12)}")


