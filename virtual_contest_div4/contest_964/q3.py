for _ in range(int(input())):
    n,s,m = map(int,input().split())
    a = 0
    b = m
    f = 0
    for i in range(n):
        l,r = map(int,input().split())
        if l-a >= s:
            f = 1
        a = r
    if m-r >= s:
        f = 1
    if f == 1:
        print("YES")
    else:
        print("NO")
        