class NumberGenerator:
    def __init__(self, num: int):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.num:
            raise StopIteration
        self.current += 1

        return self.current

for num in NumberGenerator(100):
    print(num)