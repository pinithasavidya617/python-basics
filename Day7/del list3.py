array1 =  ["A", "B", "C", "D"]
array2 = array1[:]
array3 = array2[:]
del array1[0]
del array2[:]
del array3[1]
print(array3)

