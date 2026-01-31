print("=== Filling Game ===")

print("You have to fill the word from one by one letters. You have only 8 attempts!")
word = "forest"
attempts = 0
lost_count = 0
print("F _ _ _ _ _ ")
while(attempts < 8):
    user_input = input("Guess the next letter : ")
    if(user_input == "o"):
       print("F o _ _ _ _ ")
       attempts += 1
       user_input = input("Guess the next letter : ")
       if (user_input == "s"):
             print("F o _ _ s _ ")
             attempts += 1
             user_input = input("Guess the next letter : ")
       if (user_input == "r"):
             print("F o r _ _ _ ")
             attempts += 1
             user_input = input("Guess the next letter : ")
       if (user_input == "e"):
             print("F o r e _ _ ")
             attempts += 1
             user_input = input("Guess the next letter : ")
       if (user_input == "s"):
             print("F o r e s _ ")
             attempts += 1
             user_input = input("Guess the next letter : ")
       if (user_input == "t"):
             print("F o r e s t ")
             attempts += 1
             exit("YOU WON!")
    elif(user_input == "r"):
        print("F _ r _ _ _ ")
        attempts += 1
        user_input = input("Guess the next letter : ")
        if (user_input == "r"):
            print("F o r _ _ _ ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "e"):
            print("F o r e _ _ ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "s"):
            print("F o r e s _ ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "t"):
            print("F o r e s t ")
            attempts += 1
            exit("YOU WON!")

    elif (user_input == "e"):
        print("F _ _ e _ _ ")
        attempts += 1
        user_input = input("Guess the next letter : ")
        if (user_input == "r"):
            print("F _ r e _ _ ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "o"):
            print("F o r e _ _ ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "s"):
            print("F o r e s _ ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "t"):
            print("F o r e s t ")
            attempts += 1
            exit("YOU WON!")
    elif (user_input == "s"):
        print("F _ _ _ s _ ")
        attempts += 1
        user_input = input("Guess the next letter : ")
        if (user_input == "r"):
            print("F _ r _ s _ ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "o"):
            print("F o r _ s _ ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "e"):
            print("F o r e s _ ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "t"):
            print("F o r e s t ")
            attempts += 1
            exit("YOU WON!")
    elif (user_input == "t"):
        print("F _ _ _ _ t ")
        attempts += 1
        user_input = input("Guess the next letter : ")
        if (user_input == "r"):
            print("F _ r _ _ t ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "o"):
            print("F o r _ _ t ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "e"):
            print("F o r e _ t ")
            attempts += 1
            user_input = input("Guess the next letter : ")
        if (user_input == "s"):
            print("F o r e s t ")
            attempts += 1
            exit("YOU WON!")

    else:
        lost_count += 1
        print("Try another one")
        if(lost_count == 2):
            print("hint: A place full of trees " )
        if(lost_count == 3):
            exit("You Lost!")

















































