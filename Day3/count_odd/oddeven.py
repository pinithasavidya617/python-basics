

odd_number = 0
even_number = 0
num = int(input("Enter a number: "))

while num != -1:
    if(num % 2 == 0) :
        even_number += 1



    else:
        odd_number += 1


    num = int(input("Enter a number or enter -1 to exit: "))


print(f"Count of odd numbers: {odd_number}")
print(f"Count of even numbers: {even_number}")

