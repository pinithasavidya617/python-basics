def test_scopes():
    var = 2 #function scope variable/ local variable
    x = 2
    print(f"I know this variable? {x}")
x = 1 #global scope
test_scopes()
print(x)

print("-------------")

def test_scopes2():
    global y
    y = 2
    print(f"I know this variable? {y}")
y = 1 #global scope
test_scopes2()
print(y)

print("-------------")

z = 10
def test():
    global z
    z = 15
    print(z)
test()
print(z)