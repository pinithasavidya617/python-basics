def strange_func():
    print("Hello ")

    return #after this, none executes
    print("Hello World")
    print("Hello World")


print(strange_func())
print("---------------")
def check_even_number(n):
    if n % 2 == 0:
        return "Number is even"
    print("Function is running")

print(check_even_number(7))

print("---------------")

print(check_even_number(8))
