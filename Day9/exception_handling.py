 try:
    user_input = int(input("Enter a number: "))
    print(user_input + "Hi")

except ValueError:
    user_input = int(input("Please enter valid integer : "))
    print(user_input)
except TypeError:
    print("Type error occurred")
finally:
    print("Finally block executed")

print("--------")
try:
    user_input = int(input("Enter a number: "))
    print(user_input + "Hi")

except (ValueError, TypeError):
    print("Value or Type error occurred")

finally:
    print("Finally block executed")