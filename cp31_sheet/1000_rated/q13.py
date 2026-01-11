for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    c = 0
    r = a[0]+x
    l = a[0]-x
    for i in range(1,n):
        l = max(a[i]-x,l)
        r = min(a[i]+x,r)
        if l>r:
            c += 1
            l = a[i]-x
            r = a[i]+x
    print(c)