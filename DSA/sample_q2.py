class stack:
    def __init__(self):
        self.l=[]
        self.size=0
    def push(self,v):
        self.l.append(v)
        self.size+=1
    def delete(self):
        return self.l.pop(self.size-1)
    def isempty(self):
        return self.size==0
    def peek(self):
        return self.l[self.size-1]
class node:
    def __init__(self,v):
        self.prev=None
        self.change=v
        self.u=stack()
        self.r=stack()
        self.next=None
class texteditor:
    def __init__(self):
        self.tail=None
        self.head=None
        self.size=0
    def addchange(self,c):
        new=node(c)
        print("Enter changes(-1 to stop)")
        x=input()
        while x!="-1":
            new.u.push(x)
            x=input()
        if self.size==0:
            self.head=new
            self.tail=self.head
        else:
            new.prev=self.tail
            self.tail.next=new
            self.tail=self.tail.next
        self.size+=1
    def change_existing(self,c):
        current=self.head
        for i in range(self.size):
            if current.change==c:
                break
            else:
                current=current.next
        else:
            print("Change doesn't exist!New change is created")
            self.addchange(c)
            return
        print("Enter changes(-1 to stop)")
        x=input()
        while x!="-1":
            current.u.push(x)
            x=input()
    def undo(self,c):
        current=self.head
        for i in range(self.size):
            if current.change==c:
                break
            else:
                current=current.next
        else:
            print("Change doesn't exist!")
            return
        if current.u.isempty():
            print("Nothing to undo")
            return
        y=current.u.delete()
        current.r.push(y)
        print(y,"change undone")
    def redo(self,c):
        current=self.head
        for i in range(self.size):
            if current.change==c:
                break
            else:
                current=current.next
        else:
            print("Change doesn't exist!")
            return
        if current.r.isempty():
            print("Nothing to redo")
            return
        y=current.r.delete()
        current.u.push(y)
        print(y,"change redone")
    def viewlastchange(self,c):
        current=self.head
        for i in range(self.size):
            if current.change==c:
                if not(current.u.isempty()):
                    return current.u.peek()
                else:
                    print("Undo list is empty")
                break
            else:
                current=current.next
        else:
            print("Change doesn't exist!")
            return
def main():
    editor = texteditor()

    # Adding changes
    editor.addchange("Change 1")
    editor.addchange("Change 2")

    # Modifying existing change
    editor.change_existing("Change 1")

    # Undo and redo operations
    editor.undo("Change 2")
    editor.redo("Change 2")

    # Viewing last change
    last_change = editor.viewlastchange("Change 1")
    if last_change:
        print("Last change:", last_change)
    else:
        print("No changes available")

if __name__ == "__main__":
    main()

                
