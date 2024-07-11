def mergesort(a):
    if len(a)<=1:
        return
    x=len(a)//2
    b=a[:x]
    c=a[x:]
    mergesort(b)
    mergesort(c)
    merge(a,b,c)
def merge(a,b,c):
    i,j,k=0,0,0
    while i<len(b) and j<len(c):
        if b[i]<=c[j]:
            a[k]=b[i]
            i+=1
        else:
            a[k]=c[j]
            j+=1
        k+=1
    while i<len(b):
        a[k]=b[i]
        i+=1
        k+=1
    while j<len(c):
        a[k]=c[j]
        j+=1
        k+=1
a=[5,1,2,3,7,4,8,9]
mergesort(a)
print(a)
