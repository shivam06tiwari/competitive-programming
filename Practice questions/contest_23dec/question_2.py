L = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mx = 0
    c = 0
    ind = 0
    for i in range(n-1):
        mxx = abs(a[i]-a[i+1])
        c += mxx
        mx = c
        ind = c
    for i in range(n):
        if i == 0:
            c -= abs(a[i]-a[i+1])
        elif i == n-1:
            c -= abs(a[i]-a[i-1])
        else:
            c -= abs(a[i]-a[i+1])
            c -= abs(a[i]-a[i-1])
            c += abs(a[i-1]-a[i+1])
        if c<mx:
            mx = c
        c = ind
    L.append(mx)
for ch in L:
    print(ch)