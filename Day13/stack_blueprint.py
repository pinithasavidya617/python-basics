class Stack:
    def __init__(self):
        self.__stack_list = [] #making stack list private

    def push(self, element):
        self.__stack_list.append(element)

    def pop(self):
        if len(self.__stack_list) > 0:
            val = self.__stack_list[-1]
            del self.__stack_list[-1]
            return val
        return "Stack is empty"

    def print_values(self):
        return self.__stack_list

class AddingStack(Stack): #inheritance
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0  #private attribute

    def push(self, element):  #override
        Stack.push(self, element) #super constructor
        self.__sum += element

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0

    def pop(self):
        Stack.pop(self)
        self.__count += 1

    def get_count(self):
        return self.__count





stack1 = Stack()
stack2 = Stack()

stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)

print(stack1.print_values())
print(stack2.print_values())
print(stack1.pop())
print(stack1.print_values())
print(stack2.pop())

print("-------------")

stack3 = AddingStack()

stack3.push(1)
stack3.push(5)
stack3.push(8)
stack3.push(9)
print(stack3.print_values())
print(stack3.pop())
print(stack3.get_sum())

print("-------------")

stack4 = CountingStack()
stack4.push(4)
stack4.push(5)
stack4.push(9)
print(stack4.print_values())
stack4.pop()
stack4.pop()
print(stack4.print_values())

print(stack4.get_count())

print("-------------")


counting_stack = CountingStack()

for i in range(20):
    counting_stack.push(i)
    counting_stack.pop()
print(counting_stack.get_count())




