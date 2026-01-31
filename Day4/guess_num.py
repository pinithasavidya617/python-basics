print("Guess Game!")
secret_num = 7
attempts = 1
while attempts <= 3:
    guess = int(input("Enter your guess: "))

    if guess == secret_num:
        print("Correct! You guessed it. ")
        break
    elif guess < secret_num:
        print("Too low")
    else:
        print("Too high")
    attempts += 1

if guess != secret_num:
    print("You ran out of attempts. the secret number was ", secret_num)