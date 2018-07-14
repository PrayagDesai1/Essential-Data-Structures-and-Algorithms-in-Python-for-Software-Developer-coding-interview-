"""  delete(index) - delete item at index, shifting all trailing elements left """


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
    
    def delete_at_perticular_position(self, position):
        if len(self.array) >= position:
            del self.array[position]
        else:
            print(' {} is invalid position cannot perform deletion '.format(position))
            


array = Array()
array.insert_at_end(1)
array.insert_at_end(2)
array.insert_at_end(3)
array.delete_at_perticular_position(0)
array.delete_at_perticular_position(22)
array.display()