L = []
for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = sorted(list(map(int,input().split())))
    k = -float('inf')
    f = 0
    for x in a:
        p = float('inf')
        if x >= k:
            p = x
        q = float('inf')
        w = k+x
        l, r = 0, m
        while l < r:
            d = (l+r)//2
            if b[d] < w:
                l = d+1
            else:
                r = d
        if l < m:
            q = b[l]-x
        z = min(p,q)
        if z == float('inf'):
            f = 1
            break
        k = z 
    if f == 0:
        L.append("YES")
    else:
        L.append("NO")
for ch in L:
    print(ch)
        