class queue:
    def __init__(self):
        self.l=[]
    def enqueue(self,v):
        self.l.append(v)
    def dequeue(self):
        return self.l.pop(0)
    def display(self):
        print(self.l)
    def empty(self):
        return (len(self.l)==0)
def insertion_sort_queue(queue):
    sorted_queue = []

    while not(queue.empty()):
        temp = queue.dequeue()

        while sorted_queue and sorted_queue[0] < temp:
            queue.enqueue(sorted_queue.pop(0))

        sorted_queue.append(temp)

    return sorted_queue
q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
x=insertion_sort_queue(q)
q.display()
print(x)
