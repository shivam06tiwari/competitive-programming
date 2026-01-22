for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l = []
    i = 2
    while i <= n//2:
        if n%i == 0:
            l.append(i)
        i+=1
    mx = 0
    mn = 1e9
    dif = 0
    c = 0
    for i in range(len(l)):
        z = l[i]
        for j in range(n//z):
            c = sum(a[(j*z):(j*z+z)])
            mx = max(mx,c)
            mn = min(mn,c)
        dif = max(mx-mn,dif)
        mx = 0
        mn = 1e9+1
    x = max(a)
    y = min(a)
    if x-y == 0:
        print(0)
    else:
        dif = max(x-y,dif)
        print(int(dif))