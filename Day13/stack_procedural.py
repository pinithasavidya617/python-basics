stack = []
stack2 = []# need again functions for this
def push(elem):
    stack.append(elem)

def pop():
    if len(stack) > 0:
        val = stack[-1]
        del stack[-1]
        return val
    raise Exception("Stack is empty")

try:
    push(1)
    push(2)
    push(3)
    print(stack)
    print(pop())
    print(stack)

except Exception as e:
    print(e)