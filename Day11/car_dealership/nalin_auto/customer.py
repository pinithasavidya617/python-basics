customers = [
    {"id": "001", "name" : "amal", "contact": "0254522", "purchases": [{"id": "003", "name": "byd", "model": "atto", "manufacture_year": "2005", "country_of_origin": "china"}]}
]


def add_customer (cust_id, name, contact, purchases ):
    customers.append(
        {"id" : cust_id, "name": name, "contact": contact, "purchases": purchases}
    )
    print("New customer added successfully!")


def purchase_car(cust_id, car_id, inventory):
    global customers
    wanted_customer = None
    for customer in customers:
        if customer['id'] == cust_id:
            wanted_customer = customer
            break

    if wanted_customer is None:
        print("Customer not found!")
        return None

    wanted_car = None
    for car in inventory:
        if car['id'] == car_id:
            wanted_car = car
            break

    if wanted_car is None:
        print("Car not found with that id!")
        return None

    wanted_customer['purchases'].append(wanted_car) #purchases is a list in dictionary
    print("New purchase added!")
    print(f"ID: {wanted_customer['id']} | Name: {wanted_customer['name']} | Contact: {wanted_customer['contact']} | "
          f"Purchases: {wanted_customer['purchases']}")
    return wanted_customer['purchases']


def get_customer_by_id(cust_id):
    for cust in customers:
        if cust['id'] == cust_id:
            print(f"ID: {cust['id']} | Name: {cust['name']} | Contact: {cust['contact']} | "
                  f"Purchases: {cust['purchases']}")
            return cust
    return None

# def add_customer_order(cust_id, car_info):
#     if get_customer_by_id(cust_id) is not None:
#         for cust in customers:
#             if cust['id'] == cust_id:
#                 cust['purchases'].append(car_info)

def view_all_customers():
    if customers:
        for customer in customers:
            print(f"ID: {customer['id']} | Name: {customer['name']} | Contact: {customer['contact']} | "
                  f"Purchases: {customer['purchases']}")