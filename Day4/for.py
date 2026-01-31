for i in range(10):
    print(i)

print("\n----")

for i in range(10, 20):
    print(i)

print("\n----")


for i in range(0, 20):
    print(i)
    if i == 3:
        print("exiting")
        break
    print("Hello")
print("Exited")

for i in range(0, 10, 2):
    print(i)