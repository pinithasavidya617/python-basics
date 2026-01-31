secret_number = 5
print("=== Guess Game ===")
print("You have 3 attempts to guess the number! ")
guess_num = int(input("Guess the number: "))
i = 1
while(i < 3):
    if(guess_num == secret_number):
        print("You win!")
        print("Game Over")
        break
    else:
        if (guess_num > secret_number):
            print("Too high")
        else:
            print("Too low")
        print("Try again!")
        i += 1
        guess_num = int(input("Guess the number: "))
if(i == 3):
    if(guess_num == secret_number):
        print("You win!")
    else:
        print("You Lost!")
    print("Game Over")
