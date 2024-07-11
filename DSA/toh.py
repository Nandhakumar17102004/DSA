def TOH(n,l,m,r):
    if n!=0:
        TOH(n-1,l,r,m)
        print("Move",l,"-",r)
        TOH(n-1,m,l,r)
TOH(3,1,2,3)
