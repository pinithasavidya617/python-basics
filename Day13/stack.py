stack = []

def push():
    user_input = input("Enter something: ")
    stack.append(user_input)
    return stack

def pop():
    if not stack:
        print("List is empty")
        return None
    else:
        print(f"{stack[-1]} removed")
        del stack[-1]
        

def main():
    choice = int(input("""
    Press 1 to add:
    Press 2 to pop:
    """))


    if choice == 1:
        print(push())
    elif choice == 2:
        pop()



while True:
    main()