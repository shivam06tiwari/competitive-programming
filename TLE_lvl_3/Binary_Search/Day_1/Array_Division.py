n,k = map(int,input().split())
a = list(map(int,input().split()))
l = max(a)
h = 10**15
ans = 0
while l<=h:
    m = l + (h-l)//2
    s = 0
    d = 0
    for i in range(n):
        s += a[i]
        if s > m:
            s = a[i]
            d += 1
    if d+1 <= k:
        ans = m
        h = m-1
    else:
        l = m+1
print(ans)
        
            