#take 5 words as input and put them in a list
#create a new list with words length greater than 3 characters
list1 = []
for i in range(5):
    user_input = input("Enter a word: ")
    list1.append(user_input)

list2 = [word for word in list1 if len(word) > 3]
print(list2)

list3 = [word[0] for word in list1]
print(list3)

list4 = [word[0] * 3 for word in list1]
print(list4)