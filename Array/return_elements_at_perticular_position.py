""" Return array eleemnt at given position """


class Array(object):
    
    def __init__(self):
        self.array = list()
    
    def insert(self, data):
        self.array.append(data)
    
    def display(self):
        print(self.array)
    
    def return_data_at(self, position):
        try:
            print(self.array[position])
        except IndexError:
            print('Invalid position')


array = Array()
array.insert(1)
array.insert(2)
array.insert(3)
array.display()
array.return_data_at(111)