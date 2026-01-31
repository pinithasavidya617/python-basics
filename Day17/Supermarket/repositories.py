from typing import List, Dict

from models import Product, Customer, Order
from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_by_id(self, product_id: str) -> Product:
        pass

    @abstractmethod
    def update(self, product: Product) :
        pass

    @abstractmethod
    def list_products(self) -> List[Product]:
        pass

class CustomerRepository(ABC):

    @abstractmethod
    def add(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def get_by_id(self, cust_id: str) -> Customer:
        pass

    @abstractmethod
    def list_orders(self) -> List[Customer]:
        pass


class OrderRepository(ABC):

    @abstractmethod
    def add(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def update(self, order: Order):
        pass

    @abstractmethod
    def list_orders(self) -> List[Order]:
        pass


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.__products : Dict[str: Product] = {}

    def add(self, product: Product) -> None:
        self.__products[product.product_id] = product

    def get_by_id(self, product_id: str) -> Product:
        return self.__products.get(product_id)

    def update(self, product: Product):
        self.__products[product.product_id] = product

    def list_products(self) -> List[Product]:
        return list(self.__products.values())

class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self):
        self.__customers : Dict[str: Customer] = {}

    def add(self, customer: Customer) -> None:
        self.__customers[customer.cust_id] = customer

    def get_by_id(self, cust_id: str) -> Customer:
        return self.__customers.get(cust_id)

    def list_orders(self) -> List[Customer]:
        return list(self.__customers.values())

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.__orders : Dict[str : Order] = {}

    def add(self, order: Order) -> None:
        self.__orders[order.order_id] = order

    def get_by_id(self, order_id: str) -> Order:
        return self.__orders.get(order_id)

    def update(self, order: Order):
        self.__orders[order.order_id] = order

    def list_orders(self) -> List[Order]:
        return list(self.__orders.values())