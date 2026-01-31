from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Product:
    product_id : str
    name: str
    price: float
    quantity: float

    def is_available(self) -> bool:
        return self.quantity is not None

    def add_quantity(self, add_quantity: float) -> float:
        self.quantity += add_quantity
        return self.quantity

    def reduce_quantity(self,reduce_quantity:float )-> float:
        self.quantity -= reduce_quantity
        return self.quantity


@dataclass
class Customer:
    cust_id: str
    name : str
    email : str
    phone: str

@dataclass
class OrderItem:
    product_id : str
    product_name: str
    quantity : float
    unit_price : float

    def total_price(self) -> float:
        return self.quantity * self.unit_price

@dataclass
class Order:
    order_id : str
    cust_id : str
    customer_name: str
    created_at : datetime = field(default_factory= datetime.now)
    items : List[OrderItem] = field(default_factory= list)

    def add_order(self, order: OrderItem) :
        self.items.append(order)

    def total_amount(self) -> float:
        total_amount = 0
        for item in self.items:
            total_amount += item.total_price()
        return total_amount

    def item_count(self):
        return len(self.items)





