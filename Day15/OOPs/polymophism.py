from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length + self.width

shapes: List[Shape] = [Circle(10), Rectangle(7, 5)]

for shape in shapes:
    print(shape.calculate_area())