for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    p = list(map(int,input().split()))
    xm = float("inf")
    for ch in p:
        if ch < xm:
            xm = ch
            for i in range(n):
                if a[i]%(2**ch) == 0:
                    a[i] += 2**(ch-1)
    print(*a)
            
            