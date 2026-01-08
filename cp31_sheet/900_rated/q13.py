for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0
    i = 0
    while i < n:
        if a[i] != 0:
            c += 1
            while i < n and a[i] != 0:
                i += 1
        else:
            i += 1
    if c == 0:
        print(0)
    elif c == 1:
        print(1)
    else:
        print(2)