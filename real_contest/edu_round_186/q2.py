L = []
for _ in range(int(input())):
    a,b = map(int,input().split())
    c = 0
    s1 = a
    s2 = b
    d = 0
    ba = bin(a)[2:]
    bb = bin(b)[2:]
    i = 0
    while True:
        if i%2 == 0:
            if a<2**i:
                break
            else:
                a -= 2**i
        else:
            if b<2**i:
                break
            else:
                b -= 2**i
        c += 1
        i += 1
    i = 0
    while True:
        if i%2 == 0:
            if s2<2**i:
                break
            else:
                s2 -= 2**i
        else:
            if s1<2**i:
                break
            else:
                s1 -= 2**i
        d += 1
        i += 1
    if c>=d:
        L.append(c)
    else:
        L.append(d)
for ch in L:
    print(ch)
    
        
    