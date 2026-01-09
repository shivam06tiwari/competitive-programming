for _ in range(int(input())):
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    c = 0
    p = []
    ans = 0
    for x in a:
        if x > q:
            if c >= k:
                p.append(c)
            c = 0
        else:
            c += 1
    if c >= k:
        p.append(c)
    for ele in p:
        ans += (ele-k+1)*(ele-k+2)//2
    print(ans)