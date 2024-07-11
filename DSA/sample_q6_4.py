class song:
    def __init__(self,name):
        self.sname=name
        self.count=0
        self.prev=None
        self.next=None
class playlist:
    def __init__(self,name):
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
class musicapp:
    def __init__:
        self.playlists=[]
        self.current=-1
    def addplaylist(self):
        new=playlist()
        while True:
            print("Do u want songs(y/n):")
            if ch==y:
                x=input("Enter songname:")
                new.add(x)
            else:
                break
        self.playlists.append(new)
    def playlistoptions(self,ch,p,s=None):
        if ch==1:
            self.playlists[p-1].play(n)
        elif ch==2:
            self.playlists[p-1].playnext()
        elif ch==3:
            self.playlists[p-1].playprev()
        elif ch==4:
            self.playlists[p-1].add(n)
        

            
