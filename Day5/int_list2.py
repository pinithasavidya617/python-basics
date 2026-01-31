int_list = []
tot = 0
while True:
    user_input = int(input("Enter a number: "))
    if user_input == 0:
        break
    else:
        int_list.append(user_input)
for i in int_list:
    tot += i
print(f"Sum of numbers: {tot}")
