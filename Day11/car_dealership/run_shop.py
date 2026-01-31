import time

from nalin_auto import customer, car_inventory


def main():
    print("""
    1) Add cars
    2) All Cars
    3) Search Car
    4) Cars by Prices
    5) Cars by Years
    6) Add Customer
    7) Get Customer by id
    8) Add a Purchase
    9) All customers
    10) Exit
    """)
    try:
        user_choice = int(input("Enter your choice (1-10):"))

        if user_choice == 1:
            car_id = input("Car ID : ")
            name = input("Brand name : ")
            model = input("Car model : ")
            manufacture_year = input("Manufacture year : ")
            country_of_origin = input("Country: ")
            price = int(input("Enter car price: "))

            car_inventory.add_car(car_id, name, model, manufacture_year, country_of_origin, price)

        elif user_choice == 2:
            car_inventory.show_inventory()

        elif user_choice == 3:
            user_search = input("Search a car: ")
            car_inventory.search_by_name(user_search, car_inventory.car_list)

        elif user_choice == 4:
            print(""" 
            0M - 5M range choose 1:
            5M - 10M range choose 2: """)
            choose = int(input("Enter your price range: "))

            car_inventory.car_by_prices(choose, car_inventory.car_list)



        elif user_choice == 5:
            year_input = input("Enter the year: ")
            car_inventory.car_by_year(year_input, car_inventory.car_list)

        elif user_choice == 6:
            cust_id = input("Enter new customer id: ")
            if cust_id not in customer.customers:
                cust_name = input("Enter customer name: ")
                contact = input("Enter contact num: ")
                purchases = []
                customer.add_customer(cust_id, cust_name, contact, purchases)
            else:
                print("ID already exists!")

        elif user_choice == 7:
            user_input = input("Enter user id: ")
            customer.get_customer_by_id(user_input)


        elif user_choice == 8:
            cust_id = input("Enter user id: ")
            car_inventory.show_inventory()
            car_id = input("Enter id of want to add: ")
            customer.purchase_car(cust_id, car_id, car_inventory.car_list)

        elif user_choice == 9:
            customer.view_all_customers()

        elif user_choice == 10:
            print("Thank you!")

        else:
            print("Invalid choice!")

        return user_choice

    except ValueError:
        print("Please enter an integer value!")

    except TypeError:
        print("Please enter a valid number!")


while True:
    choice = main()
    if choice in (10,): break
    if choice not in (1, 2, 3, 4, 5,6 ,7): continue