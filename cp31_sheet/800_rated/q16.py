for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if a == sorted(a):
        mx = 0
        mxx = 1e9
        for i in range(n-1):
            mx = a[i+1] - a[i]
            if mx < mxx:
                mxx = mx
        print(mxx//2+1)
    else:
        print(0)