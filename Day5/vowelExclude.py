user = input("Enter a word: ")
without_vowels = ""
for i in user:
    if i not in "aeiou" :
        without_vowels += i
print(without_vowels)



