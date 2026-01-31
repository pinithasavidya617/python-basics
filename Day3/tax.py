annual_salary = int(input("Enter your annual salary: "))

if annual_salary <= 1200000 :
    print("You have no tax")
else:
    taxable_income = annual_salary - 1200000

    if(taxable_income <= 500000):
        print(f"Your annual tax is {taxable_income * 0.06}")
    elif(taxable_income <= 1000000):
        print(f"Your annual tax is {(500000 * 0.06) + (taxable_income - 500000) * 0.12}")
    elif(taxable_income <= 1500000):
        print(f"Your annual tax is {(500000 * 0.06) + (500000 * 0.12) + (taxable_income - 1000000) * 0.18}")
    elif(taxable_income <= 2000000) :
        print(f"Your annual tax is {(500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (taxable_income - 1500000) * 0.24}")
    elif(taxable_income <= 2500000) :
        print(f"Your annual tax is {(500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + (taxable_income - 2000000) * 0.30}")
    else:
        print(f"Your annual tax is {(500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + (500000 * 0.30) + (taxable_income - 2500000) * 0.36}")




