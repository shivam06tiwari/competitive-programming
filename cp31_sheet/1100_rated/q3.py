for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        b.append([a[i],i])
    b.sort()
    p = [0]*n
    p[0] = b[0][0]
    for i in range(1,n):
        p[i] = p[i-1] + b[i][0]
    r = [0]*n
    r[n-1] = n-1
    for i in range(n-2,-1,-1):
        if p[i] >= b[i+1][0]:
            r[i] = r[i+1]
        else:
            r[i] = i
    c = [0]*n
    for i in range(n):
        c[b[i][1]] = r[i]
    print(*c)