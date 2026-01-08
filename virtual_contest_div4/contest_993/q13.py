L = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    r = sum(a)-a[0]
    ans = -r
    l =0
    t = 0
    for k in range(1,n):
        r -= a[k]
        t = a[0]+l-r
        if t>ans:
            ans = t
        l +=abs(a[k])  
    L.append(ans)
for ch in L:
    print(ch)