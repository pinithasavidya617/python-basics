numbers = [1,2,3,4,5]
numbers2 = numbers
numbers2[1] = 50
numbers[0] = 100
print(numbers)
print(numbers2)#Saves addresses , not values. So when changing a value of an index, both changes

