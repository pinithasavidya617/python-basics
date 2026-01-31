user = input("Enter a word: ").upper()
word_without_vowels = ""
vowels = "AEIOU"
for char in user:
    if char in vowels:
        continue
    else:
        word_without_vowels += char
print(word_without_vowels)