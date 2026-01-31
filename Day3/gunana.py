num = int(input("Enter a number: "))
while (num <= 12):
    i = 1
    while(i <= 12):
        print(f"{num} x {i} = {num * i}")
        i += 1
    num += 1