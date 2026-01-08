for _ in range(int(input())):
    n, k, q = map(int, input().split())
    l = [-1]*n
    h = [0]*n
    g = [0]*n
    qs = []
    for _ in range(q):
        c, a, b = map(int, input().split())
        qs.append((c,a,b))
        if c == 2:
            for i in range(a-1, b):
                h[i] = 1
        else:
            for i in range(a-1, b):
                g[i] = 1
    for c, a, b in qs:
        if c == 1:
            for i in range(a-1, b):
                if h[i] == 0:
                    l[i] = k
                    break
    for i in range(n):
        if l[i] == k:
            continue
        if g[i] == 1:
            l[i] = k + 1
        else:
            if k == 0:
                l[i] = 1
            else:
                l[i] = i % k
    print(*l,"a")
