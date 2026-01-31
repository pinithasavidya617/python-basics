#take input username

# take input price
# quantity
# is member
# when user enters price and quantity we should calculate total price
# we should write a function to give a discount if he is a member and bill amount 5000
# write a function to print the final bill with customer name


username = input("Enter the username: ")
price  = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
is_member = input("Are you a member? y/n :") == "y"

def cal_total_price(price, quantity):
    return price * quantity

total = cal_total_price(price, quantity)


def after_discount():
    dis = 0.25
    final_price  = total - (total * dis)
    print(f"{username}'s bill value is LKR {final_price}")

def final_bill():
    if total >= 5000 and is_member:
        after_discount()
    else:
        print(f"{username}'s bill value is LKR {total}" )

final_bill()




