for _ in range(int(input())):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()
    s = input()
    c = 0
    ans = []
    le = [False]*n
    d = {}
    for i in range(n):
        l = 0
        r = m-1
        while l<=r:
            mi = l + (r-l)//2
            if b[mi] > a[i]:
                r = mi-1
            else:
                l = mi+1
        if l > 0:
            if b[l-1]-a[i] not in d:
                d[b[l-1]-a[i]] = []
            d[b[l-1]-a[i]].append(i)
        if l < m:
            if b[l]-a[i] not in d:
                d[b[l]-a[i]] = []
            d[b[l]-a[i]].append(i)
    v = n
    for ch in s:
        if ch == "L":
            c -= 1
        else:
            c += 1
        if c in d:
            for hc in d[c]:
                if le[hc] == False:
                    le[hc] = True
                    v -= 1
            del d[c]
        ans.append(v)
    print(*ans)
            
                
        