for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    ans = 0
    c = a.count(-1)
    while s<0:
        s += 2
        ans += 1
        c -= 1
    if c%2 != 0:
        c -= 1
        ans += 1
    print(ans)