for i in range(int(input())):
    n = int(input())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())),reverse=True)
    ans = 1
    t = 0
    for i in range(n):
        l = 0
        r = n-1
        while l<=r:
            m = l + (r-l)//2
            if a[m] <= b[i]:
                l = m+1
            else:
                r = m-1
        ans = ans*(n-l-t)%(10**9+7)
        t += 1
        if ans == 0:
            break
    print(ans)