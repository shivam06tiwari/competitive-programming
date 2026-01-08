for _ in range(int(input())):
    n = int(input())
    c = []
    a = list(map(int,input().split()))
    c.append(a[0])
    for i in range(1,n):
        if a[i]>=a[i-1]:
            c.append(a[i])
        else:
            c.append(a[i])
            c.append(a[i])
    print(len(c))
    print(*c)
            