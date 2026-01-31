import time
pin = "0000"
amount = 5000

attempts = 0
max_attempts = 3
pin_correct = False

while attempts < max_attempts:
    pin_input = input("Enter the pin number: ")

    if pin == pin_input:
        pin_correct = True
        print("Pin Accepted!")
        break

    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Try again! You have only remaining {remaining_attempts} attempts.")

if not pin_correct: #if pin_correct == False
    time.sleep(0.5)
    exit("Too many wrong attempts. Exiting...")

while True:
    print(""" 1. Check balance
 2. Deposit money
 3. Withdraw money
 4. Exit""")
    user_input = int(input("Press the number of task you need to perform: "))
    if user_input == 1:
        print(f"Your account balance is LKR {amount} ")
        time.sleep(2)
        feed = input("Do you need to continue? y/n ")
        if feed == "n":
             exit("Thank you")

    elif user_input == 2:
        deposit = float(input("Enter the value you need to deposit: "))
        if deposit < 0:
            print("Negative values aren't support!")
            continue
        amount += deposit
        print(f"Deposit successful! ,Now your current balance is LKR {amount}")
        feed = input("Do you need to continue? y/n ")
        if feed == "n":
            exit("Thank you")
    elif user_input == 3:
         withdraw = float(input("Enter the value you need to withdraw: "))
         if withdraw < 0:
            print("Negative values aren't support!")
            continue
         if(amount > withdraw):
            amount -= withdraw
            print(f"LKR {withdraw} successfully withdrawn. Now your account balance is LKR {amount}")
         else:
            print("insufficient balance!")
            break
         feed = input("Do you need to continue? y/n ")
         if feed == "n":
            exit("Thank you")
    elif user_input == 4:
        exit("Thank you")
    else:
         print("Can't perform that action!")
         break
