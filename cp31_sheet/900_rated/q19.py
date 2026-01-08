for _ in range(int(input())):
    a,b = map(int,input().split())
    s = 0
    if b%4 == 0:
        s = 0
    elif b%4 == 1:
        s = -b
    elif b%4 == 2:
        s = 1
    else:
        s = b+1
    if a%2 == 0:
        a += s
    else:
        a -= s
    print(a)
        