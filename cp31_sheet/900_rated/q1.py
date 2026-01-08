for _ in range(int(input())):
    a,b = map(int,input().split())
    h,k = map(int,input().split())
    x,y = map(int,input().split())
    c = 0
    L = {(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)}
    lk = []
    lq = []
    for ch in L:
        m = h + ch[0]
        n = k + ch[1]
        lk.append([m,n])
    for ch in L:
        m = x + ch[0]
        n = y + ch[1]
        lq.append([m,n])
    for ch in lq:
        if ch in lk:
            c += 1
    print(c)