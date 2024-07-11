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
class node:
    def __init__(self,v,time):
        self.session=v
        self.time=time
        self.member=stack(5)
        self.next=None
class RegistrationSystem:
    def __init__(self):
        self.head=None
        self.size=0
    def addsession(self,n,t):
        new=node(n,t)
        if self.size==0 or self.head.session > n:
            new.next = self.head
            self.head = new
        else:
            current=self.head
            while current.next!=None:
                if current.session>n:
                    break
                else:
                    prev=current
                    current=current.next
            else:
                current.next=new
                return
            new.next=current
            prev.next=new
        self.size+=1
    def register(self,n,name):
        current=self.head
        while current.next!=None:
            if current.session==n:
                if current.member.capacity==current.member.size:
                    print("session",n,"is fully booked")
                    return
                current.member.push(name)
                print(name,"is added to session-",n)
                return
            else:
                current=current.next
        else:
            print("Invalid session number")
    def deregister(self,n):
        current=self.head
        while current.next!=None:
            if current.session==n:
                if current.member.isempty():
                    print("No member has registered for this session")
                    return
                y=current.member.delete()
                print(y,"is removed from session-",n)
                return
            else:
                current=current.next
        else:
            print("Invalid session number")
    def viewsessions(self):
        if self.size==0:
            print("No sessions available")
        else:
            print('Session\ttime')
            current=self.head
            while current!=None:
                print(current.session,current.time,sep='\t')
                current=current.next
if __name__ == "__main__":
    system = RegistrationSystem()

    # Add sessions
    system.addsession(1, "9:00am")
    system.addsession(2, "11:00am")
    system.addsession(3, "2:00pm")
    system.addsession(4, "4:00pm")

    # View sessions
    system.viewsessions()

    # Register attendees
    system.register(1, "Attendee 1")
    system.register(1, "Attendee 2")
    system.register(2, "Attendee 3")
    system.register(7, "Attendee 3")

    # Deregister attendee
    system.deregister(1)
    system.deregister(2)
    system.deregister(2)

    # View sessions after registration and deregistration
    system.viewsessions()
