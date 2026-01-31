cart_items = []
def add_to_cart(product, quantity):

    for item in cart_items:
        if item['product']['id'] == product['id']:
            item['quantity'] += quantity
            print(f"{product['name'] } quantity updated. Total quantity {item['quantity']}.")
            return

    cart_items.append(
        {"product" : product, "quantity" : quantity} #in this, product means 1 dictionary of products list
    )
    print(f"{product['name']} x {quantity} added to cart.")


def remove_from_cart(product_id):
    global cart_items
    #product = view_product(product_id)
    removed_item_name = None
    cart = []
    for item in cart_items:
        if item['product']['id'] != product_id:
            cart.append(item)
        else:
            removed_item_name = item['product']['name']

    cart_items.clear()
    cart_items.extend(cart)

    # cart_items = [item for item in cart_items if item ["product"]["id"] != product_id]
    # print(f"Removed product - {product['name']}")
    if removed_item_name:
        print(f"{removed_item_name} removed from the cart.")
    else:
        print(f"Product id: {product_id} not found in the list.")

def view_cart():
    if not cart_items:
        print("Your cart is empty!")
        return

    for item in cart_items:
        print(f"{item['product']['name']} * {item['quantity']}"
             f" - Price - Rs.{item['product']['price'] * item['quantity']}")

if __name__ == "__main__":

    add_to_cart({"id" : 1, "name" : "Donets" , "price": 200.0 },2)
    add_to_cart({"id": 4, "name": "Kottu", "price": 1000.0}, 3)
    view_cart()



