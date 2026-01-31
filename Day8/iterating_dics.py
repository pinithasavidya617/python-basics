student = {
    "name" : "Test",
    "age" : 20,
    "married" : True,
    "address" : "Test"
}

for keys in student.keys():
    print(keys)

for val in student.values():
    print(val)

for key,val in student.items():
    print(f"Key -> {key} | value -> {val}")