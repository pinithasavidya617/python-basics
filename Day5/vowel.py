user_input = input("Enter a word: ").upper()
word_without_vowels = ""
for char in user_input:
    if char == "A":
        continue
    elif char == "E":
        continue
    elif char == "I":
        continue
    elif char == "O":
        continue
    elif char == "U":
        continue
    else:
        word_without_vowels += char
print(word_without_vowels)