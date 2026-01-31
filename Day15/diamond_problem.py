class A:
    def a_method(self):
        print("A method")

class B(A):
    def a_method(self):
        print("Overriden by B class")
    def b_method(self):
        print("B method")

class C(A):
    def a_method(self):
        print("Overriden by C class")
    def c_method(self):
        print("C method")

class D(B, C):
    def d_method(self):
        print("D method")


d_obj = D()
d_obj.a_method()