class Engine:
    def __init__(self, capacity: str, horsepower: int):
        self.capacity = capacity
        self.horsepower = horsepower

    def start(self) -> None:
        print("GRRRRRR")



class Vehicle:
    def __init__(self, color: str, engine: Engine):
        self.color = color
        self.engine = engine

    def info(self) -> None :
        print( f"{self.engine.capacity}cc {self.engine.horsepower}HP,  {self.color} car")

eng = Engine("1200", 400)
car = Vehicle("Blue", eng)
print(car.info())