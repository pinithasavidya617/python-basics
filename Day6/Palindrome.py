word = input("Enter a word: ").lower()
test = []
for i in word:
    test.append(i)

rev = test[:]
rev.reverse()
if test == rev:
    print(f"Palindrome word: {word}")
else:
    print("Not a palindrome!")

print("--------")
print("Shorter method")

user_input = input("Enter the we word:").upper()

if user_input == user_input[::-1]: #String also a list of characters
    print(f"Palindrome word: {word}")
else:
    print("Not a palindrome!")

