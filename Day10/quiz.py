import random
#User will get random quizes
#user will need to answer
#if answer is correct he will get next question
#if not we end the game


questions = {"1": {"question" : "What is the largest country in the world? ", "answer" : "Russia"},
"2": {"question" : "Who is the founder of DIC? ", "answer" : "Anna Pojith"},



 }
while True:
    print("\nWElCOME TO QUIZ\n")
    keys_list = [q for q in questions.keys()]
    question_id = random.choice(keys_list) #using list comprehension

    user_answer = input(questions[question_id]['question'])

    if user_answer == questions[question_id]['answer']:
        print("Congrats")
    else:
        print(f"Wrong answer !. Answer is {questions[question_id]['answer']}")



