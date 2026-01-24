for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        b.append(a[i]+i+1)
    b.sort()
    c = 0
    for i in range(n):
        if k >= b[i]:
            k -= b[i]
            c += 1
    print(c)
    

