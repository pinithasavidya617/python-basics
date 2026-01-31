array1 = [
    [
        ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'],
    ],
    [   ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'],
    ],
    [ ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'],
    ]
]

print(array1[2][2][0])
print(array1[2][2][1])
print(array1[2][2][2])

print("-------------------------")

for array in array1:
    for i in array:
        for j in i:
            print(j)

print("-------------------------")

for i in range(len(array1)):
    for j in range(len(array1[i])):
        for k in range(len(array1[i][j])):
            print(array1[i][j][k])

print("---------------------------")

array2 =[[[i for i in range (2)] for i in range(3)] for i in range (4)]
print(array2)