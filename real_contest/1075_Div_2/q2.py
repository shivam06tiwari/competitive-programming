for _ in range(int(input())):
    v = 0
    g = 0
    n,x = map(int,input().split())
    for i in range(n):
        a,b,c = map(int,input().split())
        v += a*(b-1)
        g = max(g,a*b-c)
    if v >= x:
        print(0)
    elif g <= 0:
        print(-1)
    else:
        z = x-v
        print((z+g-1)//g)
    
            