for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    mx = 1
    mxx = 1
    for i in range(n-1):
        if a[i+1] - a[i] <= k:
            mx += 1
            if mxx < mx:
                mxx = mx
        else:
            mx = 1
    print(n-mxx)