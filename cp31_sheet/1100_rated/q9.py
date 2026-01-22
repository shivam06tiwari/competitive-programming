for _ in range(int(input())):
    n,z = map(int,input().split())
    l = list(map(int,input().split()))
    a = n*4
    c = 0
    b = 0
    for i in range(n):
        c += l[i]**2
        b += 4*l[i]
    c -= z
    x = (-b+(b**2-(4*a*c))**0.5)//(2*a)
    y = (-b-(b**2-(4*a*c))**0.5)//(2*a)
    print(int(max(x,y)))
        
    