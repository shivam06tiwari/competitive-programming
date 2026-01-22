for _ in range(int(input())):
    n,m,h = map(int,input().split())
    a = list(map(int,input().split()))
    c = a.copy()
    u = [-1] * n
    l = -1 
    for i in range(m):
        d,e = map(int,input().split())
        if u[d-1] <= l:
            a[d-1] = c[d-1]
        a[d-1] = a[d-1]+e
        u[d-1] = i
        if a[d-1] > h:
            l = i
    for i in range(n):
        if u[i] <= l:
            a[i] = c[i]
    print(*a)