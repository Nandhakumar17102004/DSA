class Stack:
    def __init__(self,n):
        self.l=[]
        self.top=-1
        self.size=0
        self.capacity=n
        for i in range(n):
            self.l.append(None)

    def push(self,value):
        if self.size==self.capacity:
            print("Stack overflow")
        else:
            self.top+=1
            self.l[self.top]=value
            self.size+=1

    def pop(self):
        if self.size==0:
            print("Stack Underflow")
        else:
            data=self.l[self.top]
            self.l[self.top]=None
            self.top=self.top-1
            print(data)
            self.size-=1

    def peek(self):
        if self.size==0:
            print("Stack Underflow")
        else:
            data=self.l[self.top]
            print(data)

    def peep(self,i,value):
        if self.size==0:
            print("Stack Underflow")
        else:
            self.l[self.top-i+1]=value

    def display(self):
        if self.size==0:
            return
        for i in range(self.size-1,-1,-1):
            print(self.l[i],end=" ")
        print()

s=Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
s.pop()
s.peek()
s.peep(2,19)
s.display()
