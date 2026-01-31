numbers = [1,2,3,4,5]

numbers2 = numbers[:] #Get a copy of numbers
numbers[0] = 100
print(numbers)
print(numbers2)

numbers_0_to_3 = numbers[0:3]
print(numbers_0_to_3)
print(numbers)
print("---")
print(numbers[-2:])#Last element of list