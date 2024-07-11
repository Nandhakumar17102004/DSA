class stack:
    def __init__(self):
        self.l=[]
        self.size=0
    def push(self,v):
        self.size+=1
        self.l.append(v)
    def pop(self):
        self.size-=1
        return self.l.pop()
    def isempty(self):
        return self.size==0
class song:
    def __init__(self,name):
        self.sname=name
        self.count=0
        self.prev=None
        self.next=None
class playlist:
    def __init__(self,name):
        self.pname=name
        self.head=None
        self.currentsong=None
        self.next=None
    def add(self,v):
        new=music(v)
        if self.head==None:
            self.head=new
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=new
            new.prev=current
    def play(self,v):
        current=self.head
        while current.next!=None:
            if current.sname==v:
                break
            current=current.next
        self.currentsong=current
        print(self.currentsong.sname,"is playing")
    def playnext(self):
        if self.currentsong.next==None:
            print("This is last song")
        else:
            self.currentsong=self.currentsong.next
            print(self.currentsong.sname,"is playing")
            self.currentsong.count+=1
    def playprev(self):
        if self.currentsong.prev==None:
            print("This is first song")
        else:
            self.currentsong=self.currentsong.prev
            print(self.currentsong.sname,"is playing")
            self.currentsong.count+=1
class music app:
    def __init__(self):
        self.l=[]
        self.size=0
    def addplaylist(self,v):
        new=playlist(v)
        if self.size==0:
            self.head=new
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=new
        self.size+=1
    def playlistoptions(self,ch,v,n=None):
        current=self.head
        while current.next!=None:
            if current.pname==v:
                break
            current=current.next
        else:
            print("No playlist")
            return
        if ch==1:
            current.add(n)
        elif ch==2:
            current.playnext()
        elif ch==3:
            current.playprev()
        else:
            current.play(n)
        
