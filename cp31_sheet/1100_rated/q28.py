for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.reverse()
    e = a[0]
    k = 1
    ans = 0
    while k <= n-1:
        if a[k] == e:
            k += 1
        else:
            k *= 2
            ans += 1
    print(ans)