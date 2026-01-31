import random

d = {"test" : 1, "test 2" : 2}
x = random.choice([x for x in d.keys()])

print(x)