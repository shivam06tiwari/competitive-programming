n,k = map(int,input().split())
a = list(map(int,input().split()))
l = 0
r = 10**18
ans = 0
while l<=r:
    m = l + (r-l)//2
    x = 0
    for i in range(n):
        x += m//a[i]
    if x >= k:
        ans = m
        r = m-1
    else:
        l = m+1
print(ans)