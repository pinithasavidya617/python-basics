from dataclasses import dataclass
from typing import List

from repositories import ProductRepository, CustomerRepository, OrderRepository
from models import Product, Customer, Order, OrderItem

class MarketError(Exception):
    pass

@dataclass
class MarketService:
    products : ProductRepository #composition
    customers : CustomerRepository
    orders : OrderRepository

    def add_product(self, product_id: str, name: str, price: float, quantity: float) -> Product:
        if self.products.get_by_id(product_id) is not None:
            raise MarketError("This product already exists!")

        # if self.products.get_by_id(product_id).is_available():
        #     self.products.get_by_id(product_id).add_quantity(quantity)

        if quantity < 0:
            raise MarketError("Quantity cannot be zero!")

        if price < 0:
            raise MarketError("Price cannot be less than zero!")


        product = Product(product_id, name, price, quantity)
        self.products.add(product)
        return product

    def add_customer(self, cust_id:str, name:str, email:str, phone:str):
        if self.customers.get_by_id(cust_id) is not None:
            raise MarketError("This customer already exists!")

        customer = Customer(cust_id, name, email, phone)
        self.customers.add(customer)
        return customer


    def order(self, order_id:str, cust_id:str) -> Order:
        if self.orders.get_by_id(order_id) is not None:
            raise MarketError("Order already exists!")

        cust = self.customers.get_by_id(cust_id)

        if cust is None:
            raise MarketError("Customer doesn't exist!")

        order = Order(order_id, cust_id, cust.name)
        self.orders.add(order)
        return order


    def get_all_available_product_list(self) -> List[Product]:
        return [product for product in self.products.list_products() if product.is_available()]

    def get_all_product_list(self) -> List[Product]:
        return self.products.list_products()

    def order_list(self):
        return  [ order for order in self.orders.list_orders() if order is not None]

    def add_item_to_order(self, order_id:str, product_id: str, quantity:float) -> OrderItem:
        order = self.orders.get_by_id(order_id)
        product = self.products.get_by_id(product_id)

        if order is None:
            raise MarketError("Order doesn't exist!")

        if product is None:
            raise  MarketError("Product doesn't exist!")

        if product.quantity < quantity:
            raise MarketError(f"Not enough {product.name} left")

        order_item = OrderItem(product_id, product.name, quantity, product.price)
        order.add_order(order_item)
        product.reduce_quantity(quantity)
        self.products.update(product)
        self.orders.update(order)

        return order_item

    def add_quantity(self, product_id, quantity):
        product = self.products.get_by_id(product_id)
        if product is None:
            raise MarketError("Product is unavailable!")

        if quantity < 0:
            raise MarketError("Quantity cannot be zero!")

        product.add_quantity(quantity)
        self.products.update(product)
        return product

    def reduce_quantity(self, product_id, quantity):
        product = self.products.get_by_id(product_id)
        if product is None:
            raise MarketError("Product is unavailable!")

        if quantity < 0:
            raise MarketError("Quantity cannot be zero!")

        product.reduce_quantity(quantity)
        self.products.update(product)
        return product

