for  _ in range(int(input())):
    n,k = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    p = [0]*(n+1)
    for i in range(n):
        p[i+1] = p[i] + a[i]
    mo = 0
    mxo = k
    ans = 0
    for i in range(k+1):
        c = p[n-mxo] - p[2*mo]
        ans = max(c,ans)
        mxo -= 1
        mo += 1
    print(ans)
        
    