#simple ATM machine
#pin = 0000
#amount = 5000
#User enters the pin
#has to validate whether the pin is correct and proceed
#if pin is correct show the menu
    #check balance
    #deposit money
    #withdraw money - check available balance when withdrawing , if balance is less  restrict
    #exit
#user should be able to perform those activities until he decided to exit the program
import time

pin = "0000"
amount = 5000

pin_input = input("Enter your pin: ")
time.sleep(1)

if ( pin == pin_input):
    while True:
        print(""" 1. Check balance
 2. Deposit money
 3. Withdraw money
 4. Exit""")
        user_input = int(input("Press the number of task you need to perform: "))
        if user_input == 1:
            print(f"Your account balance is LKR {amount} ")
            time.sleep(3)
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

else:
   print("Incorrect pin number!")
   exit()
