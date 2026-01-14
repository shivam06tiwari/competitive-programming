for _ in range(int(input())):
    x,y = map(int,input().split())
    xor = 0
    n = x-1
    if n%4 == 0:
        xor = n
    elif n%4 == 1:
        xor = 1
    elif n%4 == 2:
        xor = n+1
    else:
        xor = 0
    b = xor^y
    if b == 0:
        print(x)
    elif b == x:
        print(x+2)
    else:
        print(x+1)