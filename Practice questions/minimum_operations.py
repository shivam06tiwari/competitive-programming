def minimum(a,b):
    z=1
    while z<=a and b!=1:
        z*=b
    return z/b

n=int(input())
L=[]
for i in range(n):
    k,l=map(int,input().split())
    x=k
    count=0
    while x!=0:
        if x<l:
            count+=x
            x=0           
        elif x==l:
            count+=1
            x=0
        else:
            count+=1
            y=minimum(x,l)
            x-=y
    L.append(count)
for ch in L:
    print(int(ch))
           
                
                
                    