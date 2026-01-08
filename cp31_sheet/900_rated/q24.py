for i in range(int(input())):
    a,b = map(int,input().split())
    c = abs(a-b)
    if c == 0:
        print(0,0)
    else:
        m1 = min(a,b)%c
        m2 = c-min(a,b)%c
        print(c,min(m1,m2)) 