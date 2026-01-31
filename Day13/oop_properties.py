class ExampleClass:

    count = 0

    def __init__(self, val = 1):
        self.val = val #instance properties
        self.val2 = 10
        ExampleClass.count += 1

    def __str__(self): #overrided from object class(default class of python functions)
        return "Test"


test = ExampleClass() #instance/object
print(ExampleClass.count)
test2 = ExampleClass()
print(ExampleClass.count)

test.z = 20
test.x = 80 #reflection
print(test)
print(test.__dict__)#introspection