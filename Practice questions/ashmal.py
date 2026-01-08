for _ in range(int(input())):
    n = int(input())
    a = list(input().split())
    s = "" + a[0]
    for i in range(1,n):
        if s+a[i] > a[i]+s:
            s = a[i]+s
        else:
            s = s+a[i]
    print(s)