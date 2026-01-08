for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = 0
    if n%2 == 0:
        for i in range(n):
            s ^= a[i]
        if s == 0:
            print(0)
        else:
            print(-1)
    else:
        for i in range(n):
            s ^= a[i]
        print(s)