from datetime import date
expenses = []
def show_menu():
    print("\n== Expense Traker ==")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total Spent")
    print("4. Exit")

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    description = input("Enter description:")
    today = date.today()

    expense = {"amount": float(amount),
                "category": category,
                "description": str(description),
                "date": str(today)
                }

    expenses.append(expense)  #dictionary appended to list
    print("Expense added")

def view_expense():
    if not expenses:
        print("No expenses recorded yet!")
        return
    print("\n All Expenses")
    print("Amount | Category | Description | Date")
    print("--------------------------------------")

    for e in expenses:
        print(f"{e['amount']}    | {e['category']}   | {e['description']}     | {e['date']}")
    # expenses is a list of dictionaries.
    # Each 'e' in 'for e in expenses' means one dictionary (one expense).
    # e["amount"] gets the 'amount' value from that expense.
    # Example:
    # for e in expenses:
    #     print(e["amount"])
    # → prints amount from each dictionary in the list.

def view_total():
    amount = [e["amount"] for e in expenses ]
    total = sum(amount)
    print(f"\nTotal Spent: Rs. {total: .2f}")

def main():
    while True:
        show_menu()
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            view_total()
        elif choice == 4:
            print("Good Bye")
            break
        else:
            print("Invalid choice!")

main()



