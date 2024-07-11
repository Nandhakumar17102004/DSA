class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

            
    def insert(self,k):
        #@start-editable@

        self.heapList.append(k)
        self.currentSize += 1
        self.maxhipify(self.currentSize//2)
        self.printHeap()	
	    #@end-editable@

    """ This method defines the downheap function when removing min
    """
    def maxhipify(self,i):
        #@start-editable@

        while (i * 2) <= self.currentSize:
            max = self.maxChild(i)
            if self.heapList[i] < self.heapList[max]:
                self.heapList[i], self.heapList[max] = self.heapList[max], self.heapList[i]
            i = max
			
	    #@end-editable@

    def maxChild(self,i):
        #@start-editable@

        if (i * 2)+1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] > self.heapList[(i*2)+1]:
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
        self.maxhipify(1)
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
            self.maxhipify(i)
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

    def max(self):
        if len(self.heapList) == 1:
            return 'Empty heap'
        else:
            return self.heapList[1]

    def extract_max(self):
        print(self.deleteop())

    def increase_key(self, new, old):
    for i in range(len(self.heapList)):
        if self.heapList[i] == old:
            self.heapList[i] = new
            while i > 1 and self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
                i = i // 2
            self.printHeap()
            return
    print("Key not found")
        
    def heapsort(self):
        length=len(self.heapList)
        q=[]
        for i in range(length,2,-1):
            e=self.heapList[1]
            self.deleteop()
            q.append(e)
        print(q)
            

def main():
    heap = BinHeap()
    arraysize=12
    arr = [16,19,20,25,28,33,40,42,55,56,70,85]
    k=12
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
         elif (operation[0] == "M"):
              print(heap.max())
         elif (operation[0] == "E"):
              heap.extract_max()
         elif (operation[0] == "X"):
              heap.increase_key(int(operation[1]),int(operation[2]))
         elif (operation[0] == "H"):
              heap.heapsort()
              
         inputs -= 1

if __name__ == '__main__':
    main()
