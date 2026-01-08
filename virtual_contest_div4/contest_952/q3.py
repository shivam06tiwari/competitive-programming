for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0
    ans = 0
    mx = 0
    for i in range(n):
        c += a[i]
        if a[i] > mx:
            mx  = a[i]
        if c == 2*mx:
            ans += 1
    print(ans)
        