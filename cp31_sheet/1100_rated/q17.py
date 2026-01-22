d = map(int,open(0,'rb').read().split())
t = next(d)
for _ in range(t):
    n,k = next(d),next(d)
    l = []
    for i in range(n):
        p = []
        for j in range(n):
            p.append(next(d))
        l.append(p)
    c = 0
    for i in range(n//2):
        for j in range(n):
            if l[i][j] != l[n-i-1][n-j-1]:
                c += 1
        if c>k:
            print("NO")
            break
    else:
        print("YES",c)