words = ["Apple", "Encyclopedia", "Dictionary", "Red", "Blue"]
long_words = [word for word in words if len(word) >= 5]
print(long_words)
short_words = [word for word in words if len(word) <= 3]
print(short_words)
uppercase_words = [word.upper() for word in words]
print(uppercase_words)
len_word = [len(word) for word in words]
print(len_word)
vowel_word = [word for word in words if word[0].lower() in 'aeiou']
print(vowel_word)
word_info = [(word, len(word)) for word in words]
print(word_info)