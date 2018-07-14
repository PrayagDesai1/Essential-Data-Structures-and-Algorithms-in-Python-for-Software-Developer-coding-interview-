""" pop() - remove from end, return value """


class Array(object):
    
    def __init__(self):
        self.array = list()
    
    def insert_at_end(self, data):
        self.array.append(data)
    
    def display(self):
        if len(self.array) is 0:
            print('Array is empty')
        else:
            print(self.array)
    
    def pop(self):
        try:
            x = self.array[-1]
            del self.array[-1]
            return x
        except IndexError:
            print('Cannot perform pop operation. Array is empty')

            
array = Array()
array.insert_at_end(1)
array.insert_at_end(2)
array.insert_at_end(3)
print(array.pop())
print(array.pop())
print(array.pop())
array.display()