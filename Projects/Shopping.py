#Core Features

#user should be able to view the available products
#Allow user to add items to their cart by providing the product name
#User should be able to view the current cart items
#remove items from the cart
#Checkout -> list all the items upon checkout
#user should be able to clear the entire cart
#exit
import time
cart = []
products = ["Donets", "Pizza", "Submarine", "Burger", "Muffin", "Bread" ]

print()
print("-----Welcome to FRESCO-----")
print(" _ Baked Fresh, Every Day _ ")

while True:
    print("""
    1.Menu
    2.Add to cart
    3.View Cart
    4.Checkout
    5.Exit
          """)

    user_input = int(input("Select the option : "))
    if user_input == 1:
        print("\n--Our available products: ")
        print(""" 
               1.Donets      = Rs.180/=
               2.Pizza       = Rs.530/=
               3.Submarine   = Rs.280/=
               4.Burger      = Rs.500/=
               5.Muffin      = Rs.70/=
               6.Bread       = Rs.130/= 
               """)
        feed = input("Do you need to continue? y/n ")
        if feed == "y":
            print("Returning to main menu...")
            time.sleep(1)
            continue
        else:
            continue

    elif user_input == 2:

        print(""" 
        1.Donets      = Rs.180/=
        2.Pizza       = Rs.530/=
        3.Submarine   = Rs.280/=
        4.Burger      = Rs.500/=
        5.Muffin      = Rs.70/=
        6.Bread       = Rs.130/=
        
        7.Finish adding
        8.Clear the cart
        """)

        while True :

            user_choice = int(input("Enter the item number to add to cart: "))
            valid_choices = [1, 2, 3, 4, 5, 6]
            if user_choice in valid_choices:
                cart.append(products[user_choice - 1]) #Because indexes in products list starts from 0
            elif user_choice == 7:
                print("\nAdding to cart.........")
                time.sleep(2)
                print(f"Cart: {cart}")
                break
            elif user_choice == 8:
                if len(cart) == 0:
                    print("Cart is empty! ")
                else:
                    print(f"Cart: {cart}")
                    clear_whole_cart = input("\nDo you want clear the whole cart? y/n \n") == "y"

                    if clear_whole_cart:
                        print("\nClearing the cart........\n")
                        time.sleep(3)
                        cart.clear()
                        continue

                    clear_an_item = input("Do you want clear an item? y/n \n") == "y"
                    if clear_an_item:
                        for i in range(len(cart)): #To check how many indexes filled in the cart after added items, loops 3 times if length is 3
                            print(f"Position {i + 1}: {cart[i]}") #i starts with 0. We added i + 1 for show numbers starting with 1 to the user
                        cart_positions = list(range(1, len(cart)+1))#elements of range added to a list
                        choice_to_clear = int(input("Which item do you need to clear? "))
                        if choice_to_clear in cart_positions:
                            removed_item = cart.pop(choice_to_clear - 1)#Actual index in (cart) list starts with 0
                            print("\nUpdating cart.....\n")
                            time.sleep(2)
                            print(f"Removed {removed_item} from this cart")
                            print(f"Updated Cart: {cart}")
                        else:
                            print("Invalid position")

                    break
        feed = input("\nDo you want to continue? y/n ")
        if feed == "y":
            print("Returning to main menu...")
            time.sleep(1)
            continue
        else:
            continue

    elif user_input == 3:
         print(f"Cart: {cart}")
         edit_cart = input("Do you want to remove items?: y/n ") == "y"
         if edit_cart:
             clear_whole_cart = input("\nDo you want clear the whole cart? y/n \n") == "y"
             if clear_whole_cart:
                 print("\nClearing the cart........\n")
                 time.sleep(3)
                 cart.clear()
                 continue
             clear_an_item = input("Do you want clear an item? y/n \n") == "y"
             if clear_an_item:
                 for i in range(
                         len(cart)):  # To check how many indexes filled in the cart after added items, loops 3 times if length is 3
                     print( f"Position {i + 1}: {cart[i]}")  # i starts with 0. We added i + 1 for show numbers starting with 1 to the user
                 cart_positions = list(range(1, len(cart) + 1))  # elements of range added to a list
                 choice_to_clear = int(input("Which item do you need to clear? \n"))
                 if choice_to_clear in cart_positions:
                     removed_item = cart.pop(choice_to_clear - 1)  # Actual index in (cart) list starts with 0
                     print("\nUpdating cart.....\n")
                     time.sleep(2)
                     print(f"Removed {removed_item} from this cart")
                     print(f"Updated Cart: {cart}")
                 else:
                     print("Invalid position")
             continue
         else:
             feed = input("Do you want to continue? y/n ")
             if feed == "y":
                 print("Returning to main menu...")
                 time.sleep(1)
                 continue
             else:
                continue
    elif user_input == 4:
        print("\n--- Checkout ---\n")
        if len(cart) != 0:
            print(f"Here is the products that you chose: {cart}")
            while True:
                confirm = input("Do you confirm the order? : y/n: ") == "y"
                if confirm:
                    exit("Thank you for choosing FRESCO ! Enjoy your treats")
                else:
                    cancel_cart = input("Do you want to clear the cart after cancelling checkout? y/n") == "y"
                    if cancel_cart:
                        print("Clearing the cart...")
                        time.sleep(1)
                        cart.clear()
                        print("Checkout cancelling.....")
                        time.sleep(2)
                        print("\nCheckout cancelled. Returning to main menu. ")
                    else:
                        print("Checkout cancelling.....")
                        time.sleep(2)
                        print("\nCheckout cancelled. Returning to main menu. ")
                    break
        else:

            print("The cart is empty! ")
    elif user_input == 5:
        exit("Thank you!")
    else:
         print("Can't perform that action!")
         break


