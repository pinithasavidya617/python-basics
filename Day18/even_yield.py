def get_even_num(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)

    return result


def get_even_num_yield(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            yield i

for x in get_even_num_yield(20):
    print(x)

even_nums = [i for i in range(100) if i % 2 == 0] #List comprehension

even_nums_gen = (i for i in range(100) if i % 2 == 0) #Generator expression

# print(even_nums)
# print(even_nums_gen)
