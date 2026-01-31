items = []
for i in range(5):
    items.append(i + 1)
print(items)
print()

item = []
for i in range(5):
    item.insert(0, i + 1)
print(item)
# 0 index-> [1]
# 0 -> [2,1]
# 0 -> [3,2,1]
#Adding new item shifts previous items to right
print()


x = 10
y = 20
x,y = y,x
print(x,y)
print()

print("hello"[2])
