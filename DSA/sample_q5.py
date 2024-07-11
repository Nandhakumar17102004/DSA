class stack:
    def __init__(self):
        self.s=[]
        self.size=0
    def push(self,value):
        self.s.append(value)
        self.size+=1
    def delete(self):
        self.size-=1
        return self.s.pop()
    def is_empty(self):
        return self.size==0
    def display(self):
        print(self.s)
class BugTrackingSystem:
    def __init__(self):
        self.buglist={}
        self.size=0
    def add_bug(self,component,bug):
        if component in self.buglist.keys():
            self.buglist[component].push(bug)
        else:
            self.buglist[component]=stack()
            self.buglist[component].push(bug)
        self.size+=1
        print(bug,"is added to the buglist of component",component)
    def resolve_bug(self,component):
        if self.size==0:
            print("Bug list is empty")
            return
        if component not in self.buglist.keys():
            print("Invalid component.")
            return
        if self.buglist[component].is_empty():
            print(component,"doesn't have any bug left to resolve")
            return
        bug=self.buglist[component].delete()
        print(bug,"is resolved for component",component)
        self.size-=1
    def view_bug(self,component):
        if self.size==0:
            print("Bug list is empty")
            return
        if component not in self.buglist.keys():
            print("Invalid component.")
            return
        if self.buglist[component].is_empty():
            print(component,"doesn't have any bugs")
            return
        self.buglist[component].display()
def main():
    bug_tracker = BugTrackingSystem()

    while True:
        print("\nBug Tracking System")
        print("1. Add Bug")
        print("2. Resolve Bug")
        print("3. View Bugs")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            component = input("Enter component name: ")
            bug = input("Enter bug description: ")
            bug_tracker.add_bug(component, bug)

        elif choice == "2":
            component = input("Enter component name: ")
            bug_tracker.resolve_bug(component)

        elif choice == "3":
            component = input("Enter component name: ")
            bug_tracker.view_bug(component)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

        
        
