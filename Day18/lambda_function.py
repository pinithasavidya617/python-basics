add_two_num = lambda x, y : x + y #giving a name to the anonymous lambda functions

print(add_two_num(20, 82))

print((lambda x, y : x * y) (20, 50))

math_operators = {"addition " : lambda x, y : x + y,
                  "substraction": lambda x, y : x - y}

for key, val in math_operators.items():
    print(f"Operation - {key} | Val - {val(30, 20)}")

print((lambda x :  x % 2 == 0)(70))

numbers = [1, 2, 3, 4, 5, 6, 7]
doubled = list(map(lambda x : x * 2, numbers))
print(doubled)

filter_out = list(filter(lambda x : x % 2 , numbers)) #filters out
print(filter_out)
