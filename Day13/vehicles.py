class Vehicle:
    def __init__(self, brand, name, year):
        self.brand = brand
        self.name = name
        self.year = year

    def vehicle_properties(self):
        return f" This {self.brand} {self.name} made in {self.year}!"

class LandVehicles(Vehicle):
    def __init__(self, brand, name, year, fuel):
        Vehicle.__init__(self, brand, name, year)
        self.fuel = fuel

    def land_vehicle_info(self):
        return f" This {self.brand} {self.name} has a {self.fuel} engine!"

class AirVehicles(Vehicle):
    def __init__(self, brand, name, year, size):
        Vehicle.__init__(self, brand, name, year)
        self.size = size

    def air_vehicle_info(self):
        return f" This {self.brand} {self.name} is a {self.size} size aircraft!"

class Car(LandVehicles):
    def __init__(self, brand, name, year, fuel, speed):
        LandVehicles.__init__(self, brand, name, year, fuel)
        self.speed = speed

    def top_speed(self):
        return f" This {self.brand} {self.name}  can reach {self.speed}km/h as it's top speed"

class Bus(LandVehicles):
    def __init__(self, brand, name, year, fuel, seats):
        LandVehicles.__init__(self,brand,name,year,fuel)
        self.seats = seats

    def seating(self):
        return f" This {self.brand} {self.name} bus has {self.seats} seats!"


plane = AirVehicles("Boing", 747, 2017, "large")
print(plane.vehicle_properties())
print(plane.air_vehicle_info())

print("-------------")

car = Car("Nissan", "GT-R R35", 2022, "Petrol", 328)
print(car.vehicle_properties())
print(car.land_vehicle_info())
print(car.top_speed())

print("-------------")

bus = Bus("Youtong", "C12 pro", 2025, "Diesel", 48)
print(bus.vehicle_properties())
print(bus.land_vehicle_info())
print(bus.seating())

print("-------------")







