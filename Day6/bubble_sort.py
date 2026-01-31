unsorted_list = [2,5,9,1,4,6]
for j in range(len(unsorted_list) - 1):
    for i in range(len(unsorted_list) -j - 1):
        if unsorted_list[i] > unsorted_list[i + 1]:
            unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]

print(unsorted_list)