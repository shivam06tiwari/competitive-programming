for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    for j in range(q):
        l,r,k = map(int,input().split())
        c = s[n]
        c += (r-l+1)*k
        c -= s[r]
        c += s[l-1]
        if c%2 == 0:
            print("NO")
        else:
            print("YES")