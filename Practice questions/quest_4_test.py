L = []
for _ in range(int(input())):
    n = int(input())
    u = [False]*(2**n)
    c = []
    
    for i in range(n, -1, -1):
        for x in range((2**i)-1, 2**n, 2**i):
            if not u[x]:
                c.append(x)
                u[x] = True            
    L.append(c)
for ch in L:
    print(*ch)