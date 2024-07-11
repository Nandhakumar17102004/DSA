def quicksort(a,low,high):
    if low<high:
        loc=partition(a,low,high)
        quicksort(a,low,loc-1)
        quicksort(a,loc+1,high)
def partition(a,low,high):
    pivot=a[low]
    i=low
    j=high
    while i<j:
        while a[i]<=pivot:
            i+=1
        while a[j]>pivot:
            j-=1
        if i<j:
            t=a[i]
            a[i]=a[j]
            a[j]=t
    while i>j:
        t=a[low]
        a[low]=a[j]
        a[j]=t
        return j
l=[5,1,2,3,7,4,8,9]
quicksort(l,0,7)
print(l)
