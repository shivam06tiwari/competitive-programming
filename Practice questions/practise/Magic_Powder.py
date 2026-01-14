n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l = 0
r = 1e18+1
ans = 0
while l<=r:
    req = 0
    m = l + (r-l)//2
    for i in range(n):
        if a[i]*m > b[i]:
            req += a[i]*m - b[i]
    if req > k:
        r = m-1
    else:
        ans = m
        l = m+1
print(int(ans))