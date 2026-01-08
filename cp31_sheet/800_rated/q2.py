for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    mx = 0
    mxx = 0
    for i in range(n):
        if i == 0:
            mx = a[i]
            mxx = mx
        if i == n-1:
            mx = 2*(x-a[i])
            if mx > mxx:
                mxx = mx
        else:
            mx = a[i+1] - a[i]
            if mx > mxx:
                mxx = mx
    print(mxx)