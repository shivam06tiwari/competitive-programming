for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    qu = []
    z = 0
    y = 0
    for i in range(n-1,-1,-1):
        z = max(z,a[i])
        y = max(y,b[i])
        a[i] = max(z,y)
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = a[i] + s[i]
    for i in range(q):
        l,r = map(int,input().split())
        qu.append(s[r]-s[l-1])
    print(*qu)
        