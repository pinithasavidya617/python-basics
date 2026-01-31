book_names = ["Science", "Maths", "History", "ICT", "Commerce", 18, 20]

print(book_names)

print(book_names[1])

book_names[5] = "ET"

print(book_names)

print(len(book_names))

print(book_names[-1])#Access the last element

for book_name in book_names:
    print(book_name)

book_names.append("Health")#Added to last
book_names.insert(2, "Atomic Habits")#insert to 2nd place
print(book_names)

book_names.pop(3)#delete 3rd index
print(book_names)

del book_names[0]#delete an index
print(book_names)


print(help(book_names))#prints all the available methods

if "Health" in book_names:
    book_names.remove("Health")#delete by value
print(book_names)





