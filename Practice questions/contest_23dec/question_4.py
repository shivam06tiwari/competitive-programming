L = []
for _ in range(int(input())):
    n = int(input())
    c = []
    u = set()
    for i in range(n,0,-1):
        v = (2**i)-1
        c.append(v)
        u.add(v)
    for i in range(2**n):
        if i not in u:
            c.append(i)
    L.append(c)
for ch in L:
    print(*ch)