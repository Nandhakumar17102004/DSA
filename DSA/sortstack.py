class stack:
    def __init__(self,v):
        self.capacity=v
        self.l=[]
        self.size=0
        self.top=-1
    def push(self,v):
        self.l.append(v)
        self.size+=1
        self.top+=1
    def delete(self):
        self.size-=1
        y=self.l.pop(self.top)
        self.top-=1
        return y
    def isempty(self):
        return self.size==0
    def peek(self):
        if self.isempty():
            return -1
        return self.l[self.top]
    def sort(self):
        d=stack(self.capacity)
        d.push(self.delete())
        while not(self.isempty()):
            temp=self.delete()
            while temp<d.peek()and not(d.isempty()):
                self.push(d.delete())
            d.push(temp)
        return d
    def display(self):
        for i in range(self.size-1,-1,-1):
            print(self.l[i],end=' ')
        print()
        
s=stack(5)
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)

s.display()
s=s.sort()
s.display()
