int_list = []

while True:
    user_input = int(input("Enter a number: "))
    if user_input == 0:
        break
    else:
        int_list.append(user_input)
print(sum(int_list))
print(sum(int_list) / len(int_list))#Average
