import time

user_name = input("Enter your name: ")
print(f"Hello {user_name}! How can I help you? ")
user_question = input("").lower()
if user_question == "who is the richest person in the world?":
    print("Thinking...")
    time.sleep(1)
    print("The richest person in the world is Elon Musk")