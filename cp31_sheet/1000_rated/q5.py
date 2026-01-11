for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        rem = a[i] % k
        if rem == 0:
            rem = k
        b.append((-rem, i+1))
    b.sort()
    ans = []
    for x in b:
        ans.append(x[1])
    print(*ans)