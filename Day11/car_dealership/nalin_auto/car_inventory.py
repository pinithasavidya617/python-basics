car_list = []

def add_car( car_id,name,model,manufacture_year,country_of_origin,price):
    car_list.append(
        {"id" : car_id, "name" : name, "model" : model,"manufacture_year" : manufacture_year,"country_of_origin" : country_of_origin,"price" : price}
    )
    print("New Car added successfully")


def show_inventory():
    for car in car_list:
        print(f"Car ID: {car['id']}| Brand Name: {car['name']}| Model: {car['model']}| Manufacture Year: {car['manufacture_year']}| Country: {car['country_of_origin']}| Price: {car['price']}")


def find_car(user_input_id):
    for car in car_list:
        if user_input_id == car["id"]:
            return car["model"]

    return None


def search_by_name(user_entered_name, inventory):
    if not inventory:
        print("Inventory is empty!")
    for car in inventory:
        if user_entered_name == car['name']:
            print(
                f"Car ID: {car['id']}| Brand Name: {car['name']}| Model: {car['model']}| Manufacture Year: {car['manufacture_year']}| Country: {car['country_of_origin']}| Price: {car['price']}")

    return None

def car_by_prices(user_price_choice, inventory):
    if not inventory:
        print("Inventory is empty!")
    for car in inventory:
        if user_price_choice == 1: #less than 5M
            if car["price"] <= 5000000:
                print(f"Car ID: {car['id']}| Brand Name: {car['name']}| Model: {car['model']}| Manufacture Year: {car['manufacture_year']}| Country: {car['country_of_origin']}| Price: {car['price']}")
            else:
                print("No cars in inventory at this price range!")
        elif user_price_choice == 2:
            if 5000000 <= car["price"] <= 10000000 :
                 print(f"Car ID: {car['id']}| Brand Name: {car['name']}| Model: {car['model']}| Manufacture Year: {car['manufacture_year']}| Country: {car['country_of_origin']}| Price: {car['price']}"
)
            else:
                print("No cars in inventory at this price range!")
    return None

def car_by_year(user_input_year, inventory ):
    if not inventory:
        print("Inventory is empty!")

    for car in inventory:
        if user_input_year == car["manufacture_year"]:
            print(f"Car ID: {car['id']}| Brand Name: {car['name']}| Model: {car['model']}| Manufacture Year: {car['manufacture_year']}| Country: {car['country_of_origin']}| Price: {car['price']}")
        else:
            print("No car models available in this year.")
    return None






