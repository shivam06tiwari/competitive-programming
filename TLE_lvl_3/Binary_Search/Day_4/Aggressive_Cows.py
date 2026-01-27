for _ in range(int(input())):
    n,c = map(int,input().split())
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    l = 0
    r = a[-1]-a[0]
    ans = 0
    while l<=r:
        d = 0
        x = 0
        m = l + (r-l)//2
        for i in range(n-1):
            d += a[i+1]-a[i]
            if d >= m:
                d = 0
                x += 1
            if x+1 == c:
                break
        if x+1 == c:
            ans = m
            l = m+1
        else:
            r = m-1
    print(ans)
            
            
        
        