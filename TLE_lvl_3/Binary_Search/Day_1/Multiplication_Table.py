n = int(input())
l = 1
r = n*n
ans = 0
while l<=r:
    m = l + (r-l)//2
    s = 0
    for i in range(n):
        s += min(n,m//(i+1))
    if s >= (n*n+1)//2:
        ans = m
        r = m-1
    else:
        l = m+1
print(ans)