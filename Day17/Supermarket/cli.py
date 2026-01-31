from repositories import InMemoryProductRepository, InMemoryOrderRepository, InMemoryCustomerRepository
from models import Product, OrderItem, Customer,Order
from service import MarketError, MarketService

market_service = MarketService(products = InMemoryProductRepository(),
                               customers= InMemoryCustomerRepository(),
                               orders= InMemoryOrderRepository())


def add_product():
    try:
        product_id = input("Enter product_id: ")
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = float(input("Enter quantity: "))

        product = market_service.add_product(product_id, name, price, quantity)
        print(f"New product: {product.name} added successfully!")

    except TypeError as e:
        print("Type error occurred! " + str(e))

    except MarketError as e:
        print(e)
        return

def add_customer():
    try:
        cust_id = input("Enter customer id: ")
        name = input("Enter customer name: ")
        email = input("Enter email address: ")
        phone = input("Enter phone no: ")

        market_service.add_customer(cust_id, name, email, phone)
        print(f"New customer: {name} added successfully!")

    except TypeError as e:
        print("Type error occurred! " + str(e))

    except MarketError as e:
        print(e)
        return

def list_all_available_products():
    for product in market_service.get_all_available_product_list():
        print(f" Product ID - {product.product_id} | Product Name: {product.name} | Price : Rs.{product.price }|"
              f" Quantity : {product.quantity} | Availability: {product.is_available()}")

def list_all_products():
    for product in market_service.get_all_product_list():
        print(f" Product ID - {product.product_id} | Product Name: {product.name} | Price : {product.price}|"
          f" Quantity : {product.quantity} ")

def create_order():
    try:
        cust_id = input("Enter customer id: ")
        order_id = input("Enter order id: ")

        order = market_service.order(order_id, cust_id)
        print(f"Order is successfully created for customer {order.customer_name}!")
        return order_id

    except TypeError as e:
        print("Type error occurred! " + str(e))

    except MarketError as e:
        print(e)
    return None

def add_item_to_exiting_order():
    try:
        order_id = input("Enter order id: ")

        print("\n Available Products")
        list_all_available_products()

        product_id = input("Enter product_id: ")
        quantity = float(input("Enter quantity: "))

        market_service.add_item_to_order(order_id, product_id, quantity)
        print(f"Item added to order: {order_id} successfully!")
        order_summery(order_id)

    except TypeError as e:
        print("Type error occurred! " + str(e))

    except MarketError as e:
        print(e)
        return

def create_complete_order():
    print("\nCreate New Order")
    order_id = create_order()

    if order_id is None:
        return
    while True:
        print("\n Available Products")
        list_all_available_products()

        add = input("Add item to order? (y/n): ")
        if add != "y":
            break
        try:
            product_id = input("Enter product_id: ")
            quantity = float(input("Enter quantity: "))

            market_service.add_item_to_order(order_id, product_id, quantity)
            print(f"Item added to order: Order id - {order_id} successfully!")
        except TypeError as e:
            print("Type error occurred! " + str(e))

        except MarketError as e:
            print(e)
            return

    order_summery(order_id)

def order_summery(order_id):
    try:
        order = market_service.orders.get_by_id(order_id)
        if order is None:
            print("Order not found!")
            return

        print("\n Order Summery")
        print(f"Order id: {order.order_id}")
        print(f"Customer: {order.customer_name}")
        print(f"Created: {order.created_at}")
        print(f"Items: {order.item_count()}")

        if order.items:
            print("\n---Items in order---")
            for item in order.items:
                print(f" {item.product_name} : Rs.{item.unit_price} x {item.quantity}")
            print(f"Total amount: Rs.{order.total_amount()}")
        else:
            print("No items in this order!")
    except MarketError as e:
        print(e)
        return
def list_all_orders():
    orders = market_service.order_list()
    if not orders:
        print("No orders found!")
        return

    for order in orders:
        print(f"Order ID: {order.order_id} |Customer: {order.customer_name} | "
              f"Items : {order.item_count()} |Total Amount: Rs.{order.total_amount()}")

def add_quantity():
    try:

        product_id = input("Enter product_id: ")
        quantity = float(input("Enter quantity: "))

        market_service.add_quantity(product_id, quantity)
        print(f"Added new {quantity} more items successfully!")

    except TypeError as e:
        print("Type error occurred! " + str(e))

    except MarketError as e:
        print(e)
        return


def reduce_quantity():
    try:

        product_id = input("Enter product_id: ")
        quantity = float("Enter quantity: ")

        market_service.reduce_quantity(product_id, quantity)
        print(f"Removed {quantity} more items successfully!")


    except TypeError as e:
        print("Type error occurred! " + str(e))

    except MarketError as e:
        print(e)
        return


while True:

    print('''
    \n === Super Market System === \n
    1. Add product
    2. Add customer
    3. List product
    4. Create order
    5. Add items to an exiting order
    6. View order summery
    7. List orders
    8. Change quantity of products
    9. Exit \n''')

    choice = int(input("Enter choice : "))

    if choice == 1:
        add_product()

    elif choice == 2:
        add_customer()

    elif choice == 3:
        print("""
        1. All Products
        2. Available Products
        """)

        in_choice = int(input("Enter choice : "))
        if in_choice == 1:
            list_all_products()

        elif in_choice == 2:
            list_all_available_products()

    elif choice == 4:
        create_complete_order()

    elif choice == 5:
        add_item_to_exiting_order()

    elif choice == 6:
        order_id = input("Enter order id to view summery: ")
        order_summery(order_id)

    elif choice == 7:
        list_all_orders()

    elif choice == 8:
        print("""
        1. Add quantity
        2. Reduce quantity""")

        in_choice = int(input("Enter choice : "))
        if in_choice == 1:
            add_quantity()

        elif in_choice == 2:
            reduce_quantity()

    elif choice == 9:
        print("Thank you!")
        break

    else:
        print("Choose a valid option!")



