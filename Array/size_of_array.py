""" Implementation of Array size in python 3.6 """


class Array(object):
    
    def __init__(self):
        self.array = list()
    
    def insert(self, data):
        self.array.append(data)
    
    def display(self):
        print(self.array)
    
    def size(self):
        if len(self.array) is 0:
            print('size of array is 0')
        else:
            print('size of array is {} '.format(len(self.array)))


array = Array()
array.insert(1)
array.insert(2)
array.insert(3)
array.display()
array.size()
