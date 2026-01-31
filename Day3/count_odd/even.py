
i = 0
odd_number = 0
even_number = 0
while(i < 10):
    num = int(input("Enter a number: "))
    if(num % 2 == 0) :
        even_number += 1
        i = i + 1
        print("even")

    else:
        odd_number += 1
        i = i + 1
        print("odd")

print(f"Count of odd numbers: {odd_number}")
print(f"Count of even numbers: {even_number}")

