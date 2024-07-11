class queue:
    def __init__(self):
        self.size=0
        self.l=[]
    def push(self,v):
        self.size+=1
        self.l.append(v)
    def delete(self):
        self.size-=1
        return self.l.pop(0)
    def isempty(self):
        return self.size==0
class node:
    def __init__(self,v):
        self.p=v
        self.q=queue()
        self.next=None
class taskmanager:
    def __init__(self):
        self.head=None
        self.size=0
    def add(self,v,x):
        if self.size==0:
            newnode=node(x)
            self.head=newnode
            self.head.q.push(v)
            self.size+=1
        else:
            currentnode=self.head
            for i in range(self.size):
                if currentnode.p<x:
                    prev=currentnode
                    currentnode=currentnode.next
                elif currentnode.p==x:
                    currentnode.q.push(v)
                    break
                else:
                    newnode=node(x)
                    newnode.next=prev.next
                    prev.next=newnode
                    newnode.q.push(v)
                    self.size+=1
                    break
            else:
                newnode=node(x)
                prev.next=newnode
                newnode.q.push(v)
                self.size+=1
    def done(self):
        if self.size==0:
            print("Task manager is empty")
        else:
            current=self.head
            for i in range(self.size):
                if not(current.q.isempty()):
                    print("Task ",current.q.delete()," of priority",current.p,"is popped")
                    break
                else:
                    current=current.next
            else:
                print("No task is present")
                
def main():
    manager = taskmanager()

    while True:
        print("\nTask Priority Management System")
        print("1. Add a task")
        print("2. Mark a task as done")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            priority = int(input("Enter task priority: "))
            task = input("Enter task description: ")
            manager.add(task, priority)
            print("Task added successfully!")
        elif choice == "2":
            manager.done()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
