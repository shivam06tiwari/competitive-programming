for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    e = 0
    o = 0
    for ch in a:
        if ch%2 == 0:
            e += 1
        else:
            o += 1
    if o%2 == 0:
        print("YES")
    else:
        print("NO")