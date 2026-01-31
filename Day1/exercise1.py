#declare three string variables

car = "GTR"
fuel = "Petrol"


#print  variables in a single line

print(f"Car is {car} | It's fuel type is {fuel}")

#second exercise
#Declare three strings, value of the string should be city names
#print the cities in a single line separated by commas
print("-------------------------------------------------------------")
city1 = "Colombo"
city2 = "Kurunegala"
city3 = "Kandy"

print(f"{city1},{city2},{city3}")# with string formatting
print((city1) + "," + (city2) + "," + (city3))
print("Colombo", "Kurunegala", "Kandy", sep = (','))
print(city1, city2, city3, sep = (','))


#Declare a string variable and a integer variable then concatenate

name = "Pinitha"
age = 19

print("\nI am " + name + "| " + "I am " + str(age) + " years old.") # Converted int to a string value by str(...)
test = "45"
print(int(test)) # Converted an int to a string