for i in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    l = 0
    r = 10**19
    while l<=r:
        m = l + (r-l)//2
        w = 0
        for i in range(n):
            w += max(0,m-a[i])
        if w == x:
            break
        elif w < x:
            l = m+1
        else:
            r = m-1
    print(m)
        