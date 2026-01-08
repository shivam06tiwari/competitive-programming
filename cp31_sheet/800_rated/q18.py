for _ in range(int(input())):
    x,y = map(int,input().split())
    if x%y != 0:
        print(1)
        print(x)
    else:
        a = 1
        b = x-1
        while not (a%y != 0 and b%y != 0):
            a += 1
            b -= 1
        print(2)
        print(a,b)
            