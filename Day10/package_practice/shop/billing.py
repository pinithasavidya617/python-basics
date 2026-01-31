

SERVICE_CHARGE = 0.1
VAT_RATE = 0.18

def products_billing(cart_items):

    if not cart_items:
        print("Your cart is empty!")
        return None

    subtotal = 0

    for item in cart_items:
       price_for_item = item["product"]["price"] * item["quantity"]
       subtotal += price_for_item
       #print(f"{item['product']['name']} x {item['quantity']} = Rs.{price_for_item}")

    service_charge = subtotal * SERVICE_CHARGE
    vat = subtotal * VAT_RATE
    return subtotal, service_charge, vat


def shop_checkout(cart_items):
    subtotal, service_charge, vat = products_billing(cart_items)

    print("=== BILL ===")
    print(f"Subtotal - {subtotal}")
    print(f"Service Charge - {service_charge}")
    print(f"VAT - {vat}")
    print(f"Final Amount - {subtotal + vat + service_charge}")
    print("Thank you for choosing us!")
    print("Come again!")