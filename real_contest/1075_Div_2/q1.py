for _ in range(int(input())):
    n,h,l = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    c1 = 0
    c2 = 0
    d = max(h,l)
    for ch in a:
        if ch <= d:
            c1 += 1
    for ch in a:
        if ch <= min(h,l):
            c2 += 1
    print(min(c2,c1//2))
    
        