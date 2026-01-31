annual_salary = float(input("Enter the annual salary :"))
if(annual_salary < 1200000) :
    print("You are free from taxes!")
else:
    taxable_income = annual_salary - 1200000

    if(taxable_income <= 500000):
        tax = taxable_income * 0.06
    elif (taxable_income <= 1000000):
        tax = (500000 * 0.06) + ((taxable_income - 500000) * 0.12)
    elif (taxable_income <= 1500000):
        tax = ((500000 * 0.06) + (500000 * 0.12) + (taxable_income - 1000000) * 0.18)
    elif (taxable_income <= 2000000):
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + ((taxable_income - 1500000) * 0.24)
    elif (taxable_income <= 2500000):
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + ((taxable_income - 2000000) * 0.30)
    else:
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + (500000 * 0.36) + ((taxable_income - 2500000) * 0.36)

    print(f"Your tax is LKR {tax:,.2f}")
    print(f"Your annual salary after tax is LKR {(annual_salary - tax):,.2f}")

