word_list = []
frequency_count = {}
while True:

    word = input("Enter a word or enter 1 to exit: ")
    if word == "1":
        break

    word_list.append(word)

for word in word_list:
    if word in frequency_count.keys():
        frequency_count[word] += 1
    else:
        frequency_count[word] = 1

print(frequency_count)