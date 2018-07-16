""" Implement basic stack operation """


class Stack(object):


    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        self.display()

    def display(self):
        print(self.stack)
    
    def pop(self):
        try:
            x = self.stack[-1]
            del self.stack[-1]
            return x
        except IndexError:
            print("Stack is Empty ")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
