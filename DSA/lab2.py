class slist:
    class node:
        def __init__(self,value):
            self.data=value
            self.next=None
    def __init__(self):
        self.head=self.node(None)
        self.size=0
    def insertfirst(self,value):
        if self.size==0:
            self.head.data=value
        else:
            newnode=self.node(value)
            newnode.next=self.head
            self.head=newnode
        self.size+=1
    def insertlast(self,value):
        if self.size==0:
            self.head.data=value
        else:
            newnode=self.node(value)
            currentnode=self.head
            while currentnode.next!=None:
                currentnode=currentnode.next
            currentnode.next=newnode
        self.size+=1
    def insertpos(self,p,value):
        newnode=self.node(value)
        currentnode=self.head
        if p>self.size+1:
            print("Invalid")
            return
        if p==1:
            self.insertfirst(value)
            return
        for i in range(0,p-2):
            currentnode=currentnode.next
        newnode.next=currentnode.next
        currentnode.next=newnode
        self.size+=1
    def deletefirst(self):
        if self.size==0:
            print("List empty")
        elif self.size==1:
            self.head.data=None
            self.size-=1
        else:
            currentnode=self.head
            self.head=self.head.next
            del currentnode
            self.size-=1
    def deletlast(self):
        if self.size==0:
            print("list empty")
        elif self.size==1:
            self.head.data=None
            self.size-=1
        else:
            currentnode=self.head
            while currentnode.next!=None:
                prevnode=currentnode
                currentnode=currentnode.next
            prevnode.next=None
            del currentnode
            self.size-=1
    def deletepos(self,p):
        if p>self.size:
            print("Invalid")
        elif p==1:
            self.deletefirst()
        else:
            currentnode=self.head
            for i in range(0,p-1):
                prevnode=currentnode
                currentnode=currentnode.next
            prevnode.next=currentnode.next
            del currentnode
            self.size-=1
    def display(self):
        if self.size==0:
            print("Empty")
        else:
            currentnode=self.head
            while currentnode!=None:
                print(currentnode.data,end=" ")
                currentnode=currentnode.next
            print()
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def palindrome(self):
        x=[]
        currentnode=self.head
        while currentnode!=None:
            x.append(currentnode.data)
            currentnode=currentnode.next
        currentnode=self.head
        for i in range(len(x)-1,-1,-1):
            if currentnode.data!=x[i]:
                print("Not palindrome")
                break
            currentnode=currentnode.next
        else:
            print("Palindrome")
                
        
        
        
l=slist()
l.insertfirst(1)
l.insertfirst(2)
l.insertfirst(3)
l.display()
l.insertlast(1)
l.insertlast(2)
l.insertlast(3)
l.display()
l.palindrome()

