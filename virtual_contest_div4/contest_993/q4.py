for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = set()
    b = []
    ptr = 1
    for x in a:
        if x not in f:
            f.add(x)
            b.append(x)
        else:
            while ptr in f:
                ptr += 1
            f.add(ptr)
            b.append(ptr)    
    print(*b)