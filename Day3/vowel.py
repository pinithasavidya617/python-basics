x = 0
count = 0
vowel = "aeiou"
word = input("Enter a word: ")
while(x < len(word)):
    if word[x].lower() in vowel:
        count += 1
    x += 1
print(count)