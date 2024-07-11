class stack:
    def __init__(self):
        self.l=[]
        self.size=0
    def push(self,v):
        self.l.append(v)
        self.size+=1
    def delete(self,y):
        temp=stack()
        for i in range(self.size):
            x=self.l.pop()
            if x==y:
                print(x,"deregistered")
                self.size-=1
                while not(temp.isempty()):
                    self.push(temp.pop())
                break
            else:
                temp.push(x)
        else:
            print(y,"has not registered in this session")
    def isempty(self):
        return self.size==0
    def Print(self):
        print(self.l)
class registrationsystem:
    def __init__(self):
        self.event={}
    def register(self,session,name):
        if session in self.event.keys():
            self.event[session].push(name)
        else:
            self.event[session]=stack()
            self.event[session].push(name)
    def deregister(self,session,name):
        if self.event=={}:
            print("Empty")
            return
        if session not in self.event.keys():
            print("Invalid session")
        else:
            self.event[session].delete(name)
    def display(self,session):
        self.event[session].Print()

def main():
    registration_system = registrationsystem()

    while True:
        print("\nConference Registration System")
        print("1. Register attendee for a session")
        print("2. Deregister attendee from a session")
        print("3. Display attendees for a session")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            session = input("Enter session name: ")
            attendee = input("Enter attendee name: ")
            registration_system.register(session, attendee)
            print(f"{attendee} registered for {session}")

        elif choice == "2":
            session = input("Enter session name: ")
            attendee = input("Enter attendee name: ")
            registration_system.deregister(session, attendee)

        elif choice == "3":
            session = input("Enter session name: ")
            print(f"Attendees for {session}:")
            registration_system.display(session)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
