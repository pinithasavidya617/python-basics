array1 = [i for i in range (10)]
array2 = array1[1:4]
print(array2)

print("----------------")

numbers = [x for x in range(10)]
numbers_copy = []
numbers_copy.append(numbers) #appended whole list
numbers_copy.append(numbers)
numbers_copy.append(numbers[2:5])



print(numbers_copy)
print(numbers_copy[0])
print(numbers_copy[0][1])



print("----------------")

numbers_copy.extend(numbers)
numbers2 = []
numbers2.extend(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers2)
print(numbers_copy)
