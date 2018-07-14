""" Size of Linked List """
""" size is implementes in 2 ways """
""" 1> Iterating through all the nodes in linked list : size_1() """
""" 2> Keeping a class variable of LinkedList class and incrementing its value when a new node is added to the link list : size_2() """


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_beggining(self, data):
        if self.head is None:
            new_node = Node(data)
            self.size += 1
            new_node.next_node = None
            self.head = new_node
        
        else:
            new_node = Node(data)
            self.size += 1
            new_node.next_node = self.head
            self.head = new_node

    def display(self):
        current = self.head
        print('-' * 10)
        while current is not None:
            print(current.data)
            current = current.next_node
        print('-' * 10)
    
    def size_1(self):
        current = self.head
        count = 1
        while current.next_node is not None:
            count += 1
            current = current.next_node
        return count 
    
    def size_2(self):
        return self.size


ll = LinkedList()
ll.insert_at_beggining(1)
ll.insert_at_beggining(1333)
ll.insert_at_beggining(23)
ll.insert_at_beggining(2)
ll.display()
print('size of linked list is {}'.format(ll.size_1()))
print('size of linked list is {}'.format(ll.size_2()))

