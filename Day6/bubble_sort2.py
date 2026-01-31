unsorted_list = [2,5,9,1,4,6]
for j in range(len(unsorted_list) - 1):
    print("====")
    print(j)
    print(unsorted_list)
    for i in range(len(unsorted_list) - j - 1):#used - j - 1 because heaviest item already moved to the end in previous loop
        print("-----")
        print(i)
        print(f"First element {unsorted_list[i]}  Second element {unsorted_list[i + 1]}")

        if unsorted_list[i] > unsorted_list[i + 1]:
            unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
        print(f"after swap First element {unsorted_list[i]}  Second element {unsorted_list[i + 1]}")
        print("------")

print(unsorted_list)