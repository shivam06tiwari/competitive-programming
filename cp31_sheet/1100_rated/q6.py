for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    p = list(map(int,input().split()))
    b = []
    for i in range(n):
        b.append([a[i],i])
    b.sort()
    xm = float("inf")
    for ch in p:
        l = 0
        r = n-1
        while l<r:
            m = l + (r-l)//2
            if a[m] < 2**ch:
                l = m+1
            else:
                r = m-1
        print(ch,l)
        if l <= n-1 and xm > ch:
            for i in range(l,n):
                if b[i][0]%(2**ch) == 0:
                    b[i][0] += 2**(ch-1)
                    xm = ch
    for i in range(n):
        a[b[i][1]] = b[i][0]
    print(*a)
            
            