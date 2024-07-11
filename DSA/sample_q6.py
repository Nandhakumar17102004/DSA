class stack:
    def __init__(self):
        self.l=[]
        self.size=0
    def push(self,change):
        self.l.append(change)
        self.size+=1
    def delete(self):
        self.size-=1
        return self.l.pop()
    def isempty(self):
        return self.size==0
class music:
    def __init__(self,v):
        self.prev=None
        self.songname=v
        self.count=0
        self.next=None
class playlist:
    def __init__(self):
        self.head=None
        self.current=None
        self.tail=None
        sel.u=stack()
        self.r=stack()
        self.size=0
    def addsong(self,songname):
        new=music(songname)
        if self.size==0:
            self.head=new
            self.current=self.head
            self.tail=self.head
        else:
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
        self.size+=1
    def playsong(self,name):
        currentsong=self.head
        while currentsong.next!=None:
            if currentsong.songname==name:
                print(songname,"is being currently played")
                self.current=currentsong
                self.c+=1
                self.u.push(self)
                return
        print(songname,"is not available in this playlist")
    def playcurrent(self):
        self.u.push(self)
        print(self.current.songname,"is being currently played")
        return
    def playnext(self):
        if self.current.next==None:
            print("No next song")
        else:
            self.u.push(self)
            self.current=self.current.next
            print(self.current.songname,"is being currently played")
            self.current.c+=1
    def playprev(self):
        if self.current.prev==None:
            print("No previous song")
        else:
            self.u.push(self)
            self.current=self.current.prev
            print(self.current.songname,"is being currently played")
            self.current.c+=1
    def maximum(self):
        currentsong=self.head
        maxi=0
        song=None
        while currentsong.next!=None:
            if currentsong.c>maxi:
                maxi=currentsong.c
                song=currentsong.songname
        return maxi,song
    def undo(self):
        if self.u.isempty():
            print("Nothing to undo")
            return
        self.r.push(self)
        self=self.u.delete()
    def redo(self):
        if self.r.isempty():
            print("Nothing to redo")
        self.u.push(self)
        self=self.r.delete()
class node:
    def __init__(self,v):
        self.name=v
        self.songs=playlist()
        self.next=None
class musicapp:
    def __init__(self):
        self.head=None
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
    def addnewsong(self,v,s):
        current=self.head
        while current.next!=None:
            if current.name==v:
                current.addsong(s)
                print("Song added successfully")
                return
        print("Playlist doesn't exist")
    def playc(self,v):
        current=self.head
        while current.next!=None:
            if current.name==v:
                current.playcurrent()
                return
    def playd(self,v,s):
        current=self.head
        while current.next!=None:
            if current.name==v:
                current.playsong(s)
                return
    def playn(self,v):
        current=self.head
        while current.next!=None:
            if current.name==v:
                current.playnext()
                return
    def playp(self,v):
        current=self.head
        while current.next!=None:
            if current.name==v:
                current.playprev()
                return
    def up(self,v):
        current=self.head
        while current.next!=None:
            if current.name==v:
                current.undo()
                return
    def rp(self,v):
        current=self.head
        while current.next!=None:
            if current.name==v:
                current.redo()
                return
    def mostplayed(self):
        current=self.head
        a=0
        b=None
        while current.next!=None:
            x,y=current.maximum()
            if x>a:
                a=x
                b=y
        print("Most frequently played song is",b"!You have played this",a,"times.")
    def exist(self,v):
        current=self.head
        while current.next!=None:
            if current.name==v:
                return True
        return False
x=musicapp()
while True:
    print("1. Add playlist")
    print("2. Choose playlist")
    print("3. View most played song")
    print("4. Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("Enter Playlist name:")
        n=input()
        x.addplaylist(n)
        while True:
            print("Do u want to add songs(y/n)?")
            q=input()
            if q==y:
                print("Enter song name:")
                j=input()
                x.addnewsong(n,j)
            else:
                break
    elif ch==2:
        print("1)Play current song")
        print("2)Play different song")
        print("3)Play next song")
        print("4)Play previous song")
        print("5)Add song")
        print("6)Undo Playlist")
        print("7)Redo Playlist")
    
        print("Enter Playlist name:")
        n=input()
        if not(x.exist()):
            print("Playlist doesn't exist")
        else:
            print("Enter your choice")
            q=int(input())
            if q==1:
                x.playc(n)
            elif q==2:
                y=input("Enter songname")
                x.playn(n,y)
            elif q==3:
                x.playn(n)
            elif q==4:
                x.playp(n)
            elif q==5:
                print("Enter song name:")
                j=input()
                x.addnewsong(n,j)
            elif q==6:
                x.up(n)
            elif q==3:
                x.rp(n)
            else:
                print("Invalid choice")
    elif ch==3:
        x.mostplayed()
    else:
        break
