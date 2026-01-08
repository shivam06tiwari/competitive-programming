for _ in range(int(input())):
    a,b,n = map(int,input().split())
    t = b
    r = list(map(int,input().split()))
    for ch in r:
        if ch <= a-1:
            t += ch
        else:
            t += a-1
    print(t)
    