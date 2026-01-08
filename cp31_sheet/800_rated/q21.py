for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mxx = 0
    mx = 0
    for ch in a:
        if ch == 0:
            mx += 1
            if mx>mxx:
                mxx = mx
        else:
            mx = 0
    print(mxx)