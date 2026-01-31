from Day14.sampath_bank.current_account import CurrentAccount
from Day14.sampath_bank.savings import SavingsAccount, VanithaSavings
from sampath_bank.user import User
from sampath_bank.account import Account



users = []
accounts = []

def find_user(nic):
    for user in users:
        if user.get_nic() == nic:
            return user
    return None

def find_account(acc_no):
    for account in accounts:
        if account.get_account_no() == acc_no:
            return account
    return None

def list_users():
    for user in users:
        print(f" Username: {user.get_name()}|"
              f" User Age: {user.get_age()}|"
              f" User NIC: {user.get_nic()}|")

def list_account():
    for account in accounts:
        print(f"Account No: {account.get_account_no() } |"
              f"Account Balance: {account.get_account_balance()}")




while True:
    print("""
    1. Press 1 to Add an User
    2. Press 2 to Create New Account
    3. Press 3 to list all users
    4. Press 4 to list all accounts
    5. Press 5 to Deposit
    6. Press 6 to Withdraw
    7. Press 7 to View Balance
    8. Press 8 to View Cheque IDs
    9. Press 9 to Exit
    
    
    """)

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter user name: ")
        age = int(input("Enter user age: "))
        if age < 18:
            print("Age must be 18!")
            continue

        nic = input("Enter nic number: ")
        user_object = User(name, age, nic)
        users.append(user_object)
        for user in users:
            print(user)

    elif choice == 2:
        print("""
        1. Savings Account
        2. Vanitha Savings Account
        3. Current Account""")

        acc_choice = int(input("Enter your choice: "))

        acc_no = input("Enter account number: ")
        balance = float(input("Enter balance: "))
        branch = input("Enter branch: ")
        nic = input("Enter nic: ")
        user = find_user(nic)

        if not user:
            print("User Not Found!")
            continue

        if acc_choice == 1:
            atm_card_no = input("Enter the atm card no: ")
            account_object = SavingsAccount(acc_no, balance, branch, user, atm_card_no)
            print(f" New Savings account for NIC {nic} has been created successfully!")
            accounts.append(account_object)

        elif acc_choice == 2:
            atm_card_no = input("Enter the atm card no: ")
            account_object = VanithaSavings(acc_no, balance, branch, user, atm_card_no)
            print(f" New Vanitha Savings account for NIC {nic} has been created successfully!")
            accounts.append(account_object)

        elif acc_choice == 3:
            cheque_id = input("Enter the cheque id: ")
            account_object = CurrentAccount(acc_no, balance, branch, user, [cheque_id])
            print(f" New Current account for NIC {nic} has been successfully!")
            accounts.append(account_object)

    elif choice == 3:
            print(list_users())

    elif choice == 4:
            print(list_account())

    elif choice == 5:
            acc_no = input("Enter account number: ")
            account = find_account(acc_no)
            if not account:
                print("No account found for this user!")
                continue

            deposit_amount = float(input("Deposit Amount: "))
            result = account.deposit(deposit_amount)
            print(result)

    elif choice == 6:
            acc_no = input("Enter account number: ")
            account = find_account(acc_no)
            if not account:
                print("No account found for this user!")
                continue

            withdrawal_amount = int(input("Withdrawal Amount: "))
            result = account.withdraw(withdrawal_amount)
            print(result)

    elif choice == 7:
            acc_no = input("Enter account number: ")
            account = find_account(acc_no)
            print(isinstance(account, SavingsAccount))
            if not account:
                print("No account found for this user!")
                continue
            result = account.check_balance()
            print(result)

    elif choice == 8:
        cheques = []

        for account in accounts:
            if isinstance(account, CurrentAccount):
                cheques.extend(account.get_cheque_ids()) #[['125', '555', '666']]

        for cheque in cheques:
           print(cheque)

    elif choice == 9:
            print("Exiting...")
            break


    else:
        print("Invalid Choice! ")
