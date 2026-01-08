for _ in range(int(input())):
    n = int(input())
    c = []
    d = []
    f = 0
    a = list(map(int,input().split()))
    mx = max(a)
    for i in range(n):
        if a[i] == mx:
            d.append(a[i])
        else:
            c.append(a[i])
    if len(c) == 0:
        print(-1)
    else:
        print(len(c),len(d))
        print(*c)
        print(*d)