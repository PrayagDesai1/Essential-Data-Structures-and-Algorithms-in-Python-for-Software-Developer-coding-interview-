""" Implementation of Array and insertion in python 3.6 """


class Array(object):
    
    def __init__(self):
        self.array = list()
    
    def insert(self, data):
        self.array.append(data)
    
    def display(self):
        print(self.array)
    
    
array = Array()
array.insert(1)
array.insert(2)
array.insert(3)
array.display()
