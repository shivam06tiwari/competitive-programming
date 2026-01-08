for _ in range(int(input())):
    n=int(input())
    a=[0]+[*map(int,input().split())]
    L=[]
    for i in range(n):
        diff=a[i+1]-a[i]
        if i-diff>=0:
            L.append(L[i-diff])
        else:
            L.append(i+1)
    print(*L)