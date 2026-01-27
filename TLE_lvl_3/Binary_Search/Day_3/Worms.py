n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
s = [a[0]]
for i in range(1,n):
    s.append(s[i-1]+a[i])
for i in range(m):
    ans = 0
    l = 0
    h = n-1
    while l<=h:
        mid = l + (h-l)//2
        if s[mid] >= b[i]:
            ans = mid+1
            h = mid-1
        else:
            l = mid+1
    print(ans)
            