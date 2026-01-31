#one box can contain 12 eggs, when user inputs number of eggs, calculate how many boxes we can fill?
#boxes should be filled and print the remaining amount aswell
number_of_eggs = int(input("Enter number of eggs: "))
eggs_in_box = 12
number_of_boxes = number_of_eggs // eggs_in_box
print("Number of boxes: " , number_of_boxes)
remaining_amount = number_of_eggs % eggs_in_box
print("Remaining amount: ", remaining_amount)
