for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    r = sum(a)-a[0]
    summ = -r
    t = 0
    l = 0
    for k in range(1,n):
        r -= a[k]
        