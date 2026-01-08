for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    ans = 0
    for i in range(n):
        c.append((b[i],a[i]))
    c.sort()
    told = 1
    ans = k
    i = 0
    while c[i][0] < k:
        if told == n:
            break
        ans += min(c[i][1],n-told)*c[i][0]
        told += min(c[i][1],n-told)
        i += 1
    if told < n:
        ans += (n-told)*k
    print(ans)

            