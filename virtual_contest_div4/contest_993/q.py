for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    f = set(a)
    w = [x for x in range(1,n+1)]
    y = set(w)
    nf = y.difference(f)
    nfl = list(nf)
    b = [a[0]]
    f.remove(a[0])
    for i in range(n-1):
        if a[i] == a[i+1]:
            b.append(nfl[-1])
            nfl.pop()
        else:
            if a[i+1] in f:
                b.append(a[i+1])
                f.remove(a[i+1])
            else:
                b.append(nfl[-1])
                nfl.pop()
    print(*b)