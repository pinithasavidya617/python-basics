#__count__ = 0 #private variable
products = [
    {"id" : 1, "name" : "Donets" , "price": 200.0 },
    {"id": 2, "name": "Pizza", "price": 800.0},
    {"id": 3, "name": "Burger", "price": 400.0},
    {"id": 4, "name": "Kottu", "price": 1000.0},
    {"id": 5, "name": "Rice", "price": 1200.0}

]
def printing_products():
    for product in products:
        print(f" Product id. {product['id']} - {product['name']} - LKR {product['price']}")

def view_product(product_id):
    for product in products:
       if product_id == product["id"]:
           return product
    return None


if __name__ == "__main__":

    printing_products()
    user_choice = int(input("Which product do you want to view: "))
    print(view_product(user_choice))
