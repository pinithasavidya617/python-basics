#TASK
#Entry ticket price calculator
#Write a python program to calculate the final ticket price based on following rules
  #Ticket base price = LKR1000
  #Height requirement : only those who are 1.2m or taller are allowed entry
  #Discounts
     #If under 18 years old, give 20% discount
     #If 60 years or older give 50% discount

     #the program should,
     #check if the height is sufficient, apply the correct discount based on age
     #display the fina; ticket price


age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
ticket_price = 1000
discount = 0

if height < 1.20 :
    print("You are not allowed to this event...")
    exit()
else:
    print("You are allowed to this event...")

    if age < 18 :
        discount = ticket_price * 20/100
    elif age >= 60 :
        discount = ticket_price * 50/100
    else:
        discount = discount
    ticket_price -= discount
    print(f"Discount is LKR {discount}")
    print(f"Ticket Price is LKR {ticket_price}")






