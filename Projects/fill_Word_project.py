print(" === Filling Game === ")
print("""Conditions:
             You have to guess the word letter by letter,
             You have only 8 attempts, 
             And if you enter wrong letters three times, you will lost!""")
word = ["F", "_", "_", "_", "_", "_"]
attempts = 0
lost_count = 0
print("\nF _ _ _ _ _ ")
while(attempts < 8):

    user_input = input("Guess the next letter : ")
    attempts += 1
    if user_input == "o":
        word[1] = "o"
    elif user_input == "r":
        word[2] = "r"
    elif user_input == "e":
        word[3] = "e"
    elif user_input == "s":
        word[4] = "s"
    elif user_input == "t":
        word[5] = "t"
    else:
        lost_count += 1
        if lost_count == 1:
            print("Try another letter!")
        elif lost_count == 2:
            print("Try another letter!")
            print("Hint: A place full of trees")
        elif lost_count == 3:
            print("You have made three wrong guesses")
            exit("You Lost!")
        continue #Get back into loop without running the print under this

    print(
        word[0] + " " + word[1] + " " + word[2] + " " + word[3] + " " + word[4] + " " + word[5] + " ")

    if word[1] != "_" and word[2] != "_" and word[3] != "_" and word[4] != "_" and  word[5] != "_":
        exit("Congratulations, YOU WON!")

print("You have no any attempts!")