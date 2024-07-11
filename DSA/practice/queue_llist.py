class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def enqueue(self,v):
        new=node(v)
        if self.size==0:
            self.front=self.rear=new
        else:
            self.rear.next=new
            self.rear=new
        self.size+=1
    def dequeue(self):
        if self.size==0:
            print("Queue is empty")
            return
        if self.size==1:
            self.front=self.rear=None
        else:
            temp=self.front
            self.front=self.front.next
            del temp
        self.size-=1

    def display(self):
        if self.size==0:
            print("Queue is empty")
        else:
            current=self.front
            while current!=None:
                print(current.data,end=' ')
                current=current.next
            print()

    def viewfront(self):
        if self.front==None:
            return -1
        return self.front.data

    def viewrear(self):
        if self.rear==None:
            return -1
        return (self.rear.data)

if __name__ == '__main__':
    q = queue()
    q.enqueue(10)
    q.enqueue(100)
    q.display()
    q.dequeue()
    q.display()
    q.dequeue()
    q.display()
    q.dequeue()
    q.enqueue(3)
    q.display()
    q.enqueue(4)
    q.display()
    q.enqueue(5)
    q.display()
    q.dequeue()
    q.display()
    print("Queue Front : " , q.viewfront())
    print("Queue Rear : " , q.viewrear())




        
