""" Implementing queue using array """


class Queue(object):

    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        try:
            x = self.queue[0]
            del self.queue[0]
            return x
        except IndexError:
            print("Queue is empty. No dequeue operation can be performed ")
            exit

    def display_queue(self):
        print(self.queue)

    def isEmpty(self):
        if len(self.queue) is 0:
            return True
        else:
            return False


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.display_queue()

print(q.dequeue())
print(q.dequeue())
print('Is queue empty ? -> {} '.format(q.isEmpty()))
print(q.dequeue())
print('Is queue empty ? -> {} '.format(q.isEmpty()))
