list1 = [i for i in range(5)]
print(list1)
print("-----")
list2 = list1[:]
list2.extend(list1)
print(list2)
