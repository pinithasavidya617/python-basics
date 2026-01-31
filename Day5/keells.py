bill_value = float(input("Enter your bill value: "))
used_vegetables = input("Did you buy vegetables? : yer/no : ") == "yes"  # no discounts if buy veg
is_using_coupons = input("Are you using a coupon ? : yes/no : ") == "yes"  # no discounts if you use coupons
is_member = input("Are you a member? : yes/no : ") == "yes"  # members are eligible for the discount

discount = 0
is_eligible = (is_member and not used_vegetables and not is_using_coupons and bill_value > 5000)

if is_eligible:
        print("You ave 20% of discount! ")
        discount = bill_value * 0.2
        bill_value -= discount
        print(f"Bill value after discount: LKR {bill_value} ")
else:
    print("You have no discounts! ")
    print(f"Your bill value: LKR {bill_value}")
