L = []
for _ in range(int(input())):
    n,m,l,r = map(int,input().split())
    d = n-m
    if d == 0:
        L.append([l,r])
    else:
        if d > max(-l,r):
            d = d-r
            r = 0
            l = l+d
            L.append([l,r])
        else:
            if -l>r:
                l = l+d
                L.append([l,r])
            else:
                r = r-d
                L.append([l,r])   
for ch in L:
    print(*ch)