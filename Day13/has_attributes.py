class Classy:
    im_classy = "classy"
    def __init__(self):
        self.a = "aa"
        self.b = 10

    def say_hello(self):
        print("Hello world")

    def top_g(self):
        self.g = "Im top G"
        self.say_hello()



classy_object = Classy()
print(classy_object.a)
classy_object.top_g()
print(hasattr(classy_object, 'g'))

print(classy_object.__dict__)

