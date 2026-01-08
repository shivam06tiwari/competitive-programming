for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    c = 0
    c += 2*abs(a[-1] - a[0])
    c += 2*abs(a[-2] - a[1])
    print(c)