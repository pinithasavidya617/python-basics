import random

print("Rock, Paper, Scissors Game ")
choices = ['rock', 'paper', 'scissor']
user_score = 0
computer_score = 0
rounds = 1

while rounds <= 3:
    print(f"Round {rounds}")
    user_choice = input("rock / paper / scissor ? ").lower()
    computer_choice = random.choice(choices)
    print(f"Computer choice: {computer_choice}")

    if user_choice == computer_choice:
        print("Its a tie! ")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
    (user_choice == "paper" and computer_choice == "rock") or \
    (user_choice == "scissor" and computer_choice == "paper") :
        print("You win this round.")
        user_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1
    rounds += 1
print("\nGame over!")
print(f"Your score: {user_score}")
print(f"Computer score: {computer_score}")

if user_score < computer_score:
    print("Computer wins the game!")
elif user_score > computer_score:
    print("You are the winner!")
else:
    print("Game tied!")

