class stack:
    def __init__(self,m,n):
        self.l=[]
        self.top=[]
        self.end=[]
        for i in range(0,m*n,m):
            self.top.append(i-1)
            self.end.append(i+m-1)
        for i in range(0,m*n):
            self.l.append(None)
    def push(self,value,k):
        if self.top[k-1]<=self.end[k-1]:
            self.top[k-1]+=1
            self.l[self.top[k-1]]=value
        else:
            print(k,"th stack is full",sep='')
    def pop(self,k):
        if k==1:
            if self.top[0]==-1:
                print("Stack",k,"is empty")
            else:
                self.l[self.top[k-1]]=None
                self.top[0]-=1
        else:
            if self.top[k-1]==self.end[k-2]:
                print("Stack",k,"is empty")
            else:
                self.l[self.top[k-1]]=None
                self.top[k-1]-=1
    def display(self):
        print(self.l)
s=stack(3,3)
s.push(10,1)
s.push(20,1)
s.push(10,2)
s.push(20,2)
s.push(10,3)
s.push(20,3)
s.pop(1)
s.display()
s.pop(2)
s.display()
s.pop(3)
s.display()
s.pop(1)
s.display()
