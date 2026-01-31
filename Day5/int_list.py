#Take input as numbers from user when user finishes inserting numbers
#he can input 0 when he is done
#put all user input numbers to a list
#Then sum up the numbers
int_list = []
tot = 0
while True:
    user_input = int(input("Enter a number: "))
    int_list.append(user_input)
    if user_input == 0:
        for i in int_list:
            tot += i
        print(f"Sum of numbers: {tot}")
        break



