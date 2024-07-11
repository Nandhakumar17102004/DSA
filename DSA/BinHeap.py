class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    """ This method defines the upheap function when inserting an element"""
    
    def upHeapp(self,i):
        #@start-editable@

        while i//2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2
			
	    #@end-editable@
    
            
    def insert(self,k):
        #@start-editable@

        self.heapList.append(k)
        self.currentSize += 1
        self.downHeap(self.currentSize//2)
        self.printHeap()	
	    #@end-editable@

    """ This method defines the downheap function when removing min
    """
    def downHeap(self,i):
        #@start-editable@

        while (i * 2) <= self.currentSize:
            min = self.minChild(i)
            if self.heapList[i] > self.heapList[min]:
                self.heapList[i], self.heapList[min] = self.heapList[min], self.heapList[i]
            i = min
			
	    #@end-editable@

    def minChild(self,i):
        #@start-editable@

        if (i * 2)+1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
			
	    #@end-editable@

    def deleteop(self):
        #@start-editable@

        if len(self.heapList) == 1:
            return 'Empty heap'
        root = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop(self.currentSize)
        self.currentSize -= 1
        self.downHeap(1)
        self.printHeap()
        return root
    			
	    #@end-editable@
    
    def buildHeap(self,alist,k):
        #@start-editable@
        tempalist=list()
        for i in range(k):
            tempalist.append(alist[i])
        i = len(tempalist) // 2
        self.currentSize = len(tempalist)
        self.heapList = [0] + tempalist[:]
        while (i > 0):  #// \label{lst:bh:loop}
            self.downHeap(i)
            i = i - 1
        #@end-editable@
        self.printHeap()


    #create a method to print the contents of the heap in level order 
    def printHeap(self):
        print(self.heapList)
        
    def klargest(self,alist,k):
        #@start-editable@
        temp=k
        length=len(alist)
        while(temp<length):
            if (self.heapList[1]<alist[temp]):
                self.deleteop()
                self.insert(alist[temp])
            temp+=1
            
        #@end-editable@
        return self.heapList[1]

def main():
    heap = BinHeap()
    arraysize=int(input())
    arr = list(map(int, input().split()))
    k=int(input())
    heap.buildHeap(arr,arraysize)
    inputs = int(input())
    while inputs > 0:
         command = input()
         operation = command.split()
         if (operation[0] == "I"):
              heap.insert(int(operation[1]))
              
         elif (operation[0] == "D"):
              heap.deleteop()
              
         elif (operation[0] == "K"):
              kthlargest=heap.klargest(arr,k)
              print(kthlargest)
              
         inputs -= 1

if __name__ == '__main__':
    main()
