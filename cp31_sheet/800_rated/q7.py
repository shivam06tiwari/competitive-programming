for _ in range(int(input())):
    n,k = map(int,input().split())
    x = input()
    s = input()
    c = 0
    while s not in x:
        x = 2*x
        c += 1
        if c>5:
            c = -1
            break
    print(c)
        