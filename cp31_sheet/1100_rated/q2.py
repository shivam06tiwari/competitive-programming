for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    mx = 0
    sc = 0
    sm = 0
    ans = 0
    for i in range(0,min(n,k)):
        mx = max(mx,b[i])
        sm += a[i]
        sc = sm + mx*(max(0,k-i-1))
        ans = max(ans,sc)
    print(ans)
        
        