class queue:
    def __init__(self):
        self.l=[]
    def push(self,value):
        self.l.append(value)
class node:
    def __init__(self,tno,size):
        self.tableno=tno
        self.q=queue()
        self.size=size
        self.capacity=6
        self.next=None
class ReservationSystem:
    def __init__(self):
        self.head=None
        self.size=0
    def add(self,tno,time,size):
        if tno<=0 or tno>10:
            print("Invalid table number. Enter values between 1 to 10")
            return
        if int(time)<0 or int(time)>23:
            print("Invalid time. Enter values between 0:00 to 10")
            return
        if self.size==0:
            newnode=node(tno)
            self.head=newnode
            if size>self.head.q.capacity:
                print("Table is small. Kindly book other table")
                return
            self.head.q.push(time)
        else:
            currentnode=self.head
            for i in range(self.size):
                prev=currentnode
                if currentnode.tableno==tno:
                    if time in currentnode.q:
                        print("Already Reserved")
                    else:
                        if size>self.currentnode.q.capacity:
                            print("Table is small. Kindly book other table")
                            return
                        currentnode.q.push(time)
                    break
                else:
                    currentnode=currentnode.next
            else:
                newnode=node(tno)
                prev.next=newnode
                if size>self.newnode.q.capacity:
                    print("Table is small. Kindly book other table")
                    return
                newnode.q.push(time)


def main():
    reservation_system = ReservationSystem()

    while True:
        print("\nRestaurant Reservation System")
        print("1. Add reservation")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            table_number = int(input("Enter table number(1-10): "))
            reservation_time = input("Enter reservation time (0:00-23:00): ")
            members=int(input("Enter number of people:"))
            reservation_system.add(table_number, reservation_time)


        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()
