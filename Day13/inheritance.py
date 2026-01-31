class Animal: #Generic
    def __init__(self, scientific_name, color):
        self.scientific_name = scientific_name
        self.color = color

    def eat(self):
        print(f"{self.scientific_name} is eating")

    def sleep(self):
        print(f"{self.scientific_name} is sleeping")

class Mammal(Animal):#Inherit (is-a)
    def __init__(self, scientific_name, color, breed):
        Animal.__init__(self,scientific_name, color)
        self.breed = breed

    def drinking_milk(self):
        print(f"{self.scientific_name} with {self.breed} is drinking milk")

class Dog(Mammal):
    def __init__(self, color, breed, tail):
        Mammal.__init__(self,"dogiliyo dog", color, breed)
        self.tail = tail

dog = Mammal("dogiliyo dog", "black", "BullDog" )
dog.drinking_milk()
dog.eat()
print(isinstance(dog, Animal))
print(issubclass(Mammal, Animal))

print("------")

dog2 = Dog("black", "Bully", False)
dog2.eat()
dog2.drinking_milk()