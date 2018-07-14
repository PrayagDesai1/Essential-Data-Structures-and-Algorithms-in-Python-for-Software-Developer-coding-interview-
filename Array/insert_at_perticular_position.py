""" Insert element at perticular position in array """
""" additional function used -> list.insert() """


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
    
    def insert_at_perticular_position(self, position, data):
        if len(self.array) >= position:
            self.array.insert(position, data)
        else:
            print(' {} is invalid position cannot perform insertion '.format(position))
            


array = Array()
array.insert_at_end(1)
array.insert_at_end(2)
array.insert_at_end(3)
array.insert_at_perticular_position(3,222)
array.insert_at_perticular_position(22,100)
array.display()