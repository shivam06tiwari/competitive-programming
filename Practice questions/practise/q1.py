for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    l = [x for x in range(1,n+1)]
    r = [x for x in range(n+1,2*n+1)]
    for i in range(n//2):
        if i%2 == 0:
            a.append(r[-1])
            a.append(l[-1])
            r.pop()
            l.pop()
            b.append(l[-1])
            b.append(r[-1])
            r.pop()
            l.pop()
        else:
            a.append(r[-1])
            a.append(l[-1])
            r.pop()
            l.pop()
            b.append(l[-1])
            b.append(r[-1])
            r.pop()
            l.pop()
    print(*a)
    print(*b)