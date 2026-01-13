n = int(input())
a = list(map(int,input().split()))
q = int(input())
a.sort()
for i in range(q):
    t = int(input())
    ans = 0
    l = 0
    r = n-1
    while l<=r:
        m = l + (r-l)//2
        if a[m] <= t:
            ans = m
            l = m+1
        else:
            r = m-1
    if t<a[0]:
        print(0)
    else:
        print(ans+1)