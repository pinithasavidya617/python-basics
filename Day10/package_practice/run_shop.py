import time
from shop import products, cart, billing
# from Day10.package_practice.shop import cart
# from Day10.package_practice.shop.billing import products_billing, shop_checkout
# from Day10.package_practice.shop.cart import add_to_cart, remove_from_cart, view_cart, cart_items
# from Day10.package_practice.shop.products import view_product, printing_products
#

from shop import billing, cart, products

def main():
    print("""
    1. All Products
    2. Add to Cart
    3. Remove From Cart
    4. View Cart
    5. Checkout
    6. Exit
    """)
    try:
        choice = int(input("Enter your choice (1-6):"))

        if choice == 1:
            products.printing_products()


        elif choice == 2:
            products.printing_products()
            product_id = int(input("\nWhich product do you want to add: "))
            # product = input("Which item do you want to add: ")
            quantity = int(input("Quantity of you want: "))
            if quantity <= 0:
                print("Please enter a valid quantity! ")
                return choice

            cart.add_to_cart(products.view_product(product_id), quantity)
            # add_to_cart(product, quantity)


        elif choice == 3:
            if not cart.cart_items:
                print("Your cart is empty!")
                return choice

            cart.view_cart()
            product_id = int(input("Which product do you want to remove: "))
            cart.remove_from_cart(product_id)


        elif choice == 4:
            cart.view_cart()


        elif choice == 5:

            print("Processing your bill...")
            time.sleep(0.25)
            billing.products_billing(cart.cart_items)
            billing.shop_checkout(cart.cart_items)
            cart.cart_items.clear()


        elif choice == 6:
            print("Thank you!")


        else:
            print("Invalid choice!")

        return choice

    except ValueError:
        print("Please enter an integer value!")

    except TypeError:
        print("Please enter a valid number!")



while True:
   choice = main()
   if choice in (6,): break
   if choice not in (1, 2, 3, 4, 5 ) : continue