""" LinkedList implementation and Insert node at beggining of Linked List """


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def insert_at_beggining(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next_node = None
            self.head = new_node
        
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node

    def display(self):
        current = self.head
        print('-' * 10)
        while current is not None:
            print(current.data)
            current = current.next_node
        print('-' * 10)


ll = LinkedList()
ll.insert_at_beggining(1)
ll.insert_at_beggining(1333)
ll.insert_at_beggining(23)
ll.insert_at_beggining(2)
ll.display()