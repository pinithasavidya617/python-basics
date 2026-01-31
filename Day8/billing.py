def calculate_total_price(quantity, price):
    return price * quantity
def calculate_final_price(bill_value, membership_status):
    if bill_value >= 5000 and membership_status:
        return bill_value * 0.8
    else:
        return bill_value

def get_print(name, last_price):
    print(f"{name}'s bill value is LKR {last_price}")




username = input("Enter the username: ")
user_price  = float(input("Enter the price: "))
user_quantity = int(input("Enter the quantity: "))
is_member = input("Are you a member? y/n :") == "y"

total = calculate_total_price(user_quantity, user_price)
final_price = calculate_final_price(total, is_member)
get_print(username, final_price)
