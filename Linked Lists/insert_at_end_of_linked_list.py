""" LinkedList : Insert at end of Singular Linked List """


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next_node = None
            self.head = new_node
        
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            new_node = Node(data)
            current.next_node = new_node
            new_node.next_node = None
            print('success')

    def display(self):
        current = self.head
        print('-' * 10)
        while current is not None:
            print(current.data)
            current = current.next_node
        print('-' * 10)


ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(1333)
ll.insert_at_end(23)
ll.insert_at_end(2)
ll.display()