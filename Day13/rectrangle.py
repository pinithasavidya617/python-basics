class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area = self.height * self.width
        return area

    def perimeter(self):
        perimeter = (self.height * 2) + (self.width * 2)
        return perimeter

rectangle1 = Rectangle(25, 96)
print(rectangle1.area())
print(rectangle1.perimeter())