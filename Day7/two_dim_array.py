two_dim_array = [["x", "x", "x"],
                 ["x", "x", "x"],
                 ["x", "x", "x"],
                 ["x", "x", "x"]]


two_dim_array[1][1] = "b"
print(two_dim_array)
print('---------------')
for array in two_dim_array:
    print(array)
    for i in array:
         print(i, end="") #output can get to one line by end

letters = ["x"]