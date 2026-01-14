import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    p = 1e9
    c = b
    if a == b:
        print(2)
    elif b>a:
        print(1)
    else:
        t = 0
        lg = 0
        z = a
        if b == 1:
            c += 1
        while z > 0:
            z //= c
            lg +=1
        t = c-b+ lg
        while t <= p:
            p = t
            c += 1
            z = a
            lg = 0
            while z > 0:
                z //= c
                lg +=1
            t = c-b+ lg
        print(p)
        
        