text = 'x'
try:
    while True :
        text = text + text
        print(len(text))

except MemoryError :
    print("error")