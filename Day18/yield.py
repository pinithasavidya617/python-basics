import time
#yield = Useful for reading large files, streaming data, etc., without loading everything at once.

def generate_numbers():
    yield 10
    yield 11
    yield 12
    yield 15

gen = generate_numbers()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def create_large_list(n):
    return list(range(n))

def create_large_yield_list(n):#More memory efficient
    for i in range(n):
        yield i


start_time = time.time()
print(f"List create time - {start_time}")
large_list = create_large_list(10000000) #slower
end_time = time.time()
print(f"List end time {end_time}")

yield_start_time = time.time()
print(f"List create time - {yield_start_time}")
yield_large_list = create_large_yield_list(10000000) #faster
end_time = time.time()
print(f"List end time {end_time}")

def infinite_numbers():
    n = 1
    while True:
        yield n
        n += 1

gen = infinite_numbers()
for _ in range(5):
    print(next(gen))  # 1,2,3,4,5

