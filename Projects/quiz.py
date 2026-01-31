questions = [
    ["What is the capital of Sri Lanka? "],
    ["What is the main dish in Sri Lanka?"],
    ["Who is the president of Sri Lanka"],
    ["What is the highest trim level of Range Rovers? "],
    ["Which car can reach upto 300Km/h?  "]]

options = [
    ["A. Kandy", "B. Colombo", "C. Jayawardenapura", "4. Kurunegala" ],
    ["A. Bread", "B. Rice", "C. Noodles", "D. Hoppers" ],
    ["A. AKD", "B. RW", "C. MR", "D. GR"],
    ["A. Sport", "B. Vogue", "C. Velar", "D. Autobiography"],
    ["A. Toyota Crown", "B. Nissan GTR R35", "C. Tesla Model S", "D. Lancer EVO X "]]

answers = ["C", "B", "A", "D", "B"]
score = 0

for i in range(len(questions)):
    print("\nQuestion", i + 1)
    print(questions[i])
    for option in options[i]:
        print(option)

    user_input = input("Enter your answer A/B/C/D ? ").upper()

    if user_input == answers[i]:
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT ANSWER!")

print("Quiz over")
print("\nYour score:", score,"/",len(questions))


