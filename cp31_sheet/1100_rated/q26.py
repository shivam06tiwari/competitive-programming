for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l = 0
    r = n-1
    ans = 0
    s1 = a[l]
    s2 = a[r]
    while l<r:
        if s1 == s2:
            ans = l+1 + n-r
            l += 1
            s1 += a[l]
        elif s1 > s2:
            r -= 1
            s2 += a[r]
        else:
            l += 1
            s1 += a[l]
    print(ans)