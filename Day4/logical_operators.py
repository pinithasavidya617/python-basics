#if a number is divisible by 3 print fizz
#if a number is divisible by 5 print buzz
#if do both print fizzbuzz
for num in range(0, 100):
    if num % 3 == 0 and num % 5 == 0:
        print(num, "fizzbuzz")
    elif num % 3 == 0:
            print(num, "fizz")
    elif num % 5 == 0:
            print(num, "buzz")
    else:
        print(num)
