elements = [1,1,2,2,3,5,6,7,7,8]
unique_values = []
for element in elements:
    if element not in unique_values:
        unique_values.append(element)
elements = unique_values[:]
print(elements)