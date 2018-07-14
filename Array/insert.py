""" find(item) - looks for value and returns first index with that value, -1 if not found """


class Array(object):
    
    def __init__(self):
        self.array = list()
    
    def insert_at_end(self, data):
        self.array.append(data)
    
    def display(self):
        if self.array is None:
            print('Array is empty')
        else:
            print(self.array)
    
    def find(self, data):
        for i in range(len(self.array)):
            if self.array[i] is data:
                print(i)
            else:
                pass

array = Array()
array.insert_at_end(1)
array.insert_at_end(2)
array.insert_at_end(3)
array.insert_at_end(2)
array.insert_at_end(3)
array.insert_at_end(1)
array.find(1)
array.display()