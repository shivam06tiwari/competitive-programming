for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = a.copy()
    c.sort()
    if a == c:
        print(-1)
    else:
        l = []
        mn = c[0]
        mx = c[-1]
        for i in range(n):
            if a[i] != c[i]:
                if a[i] != mx and a[i] != mn:
                    z = max(mx-a[i],a[i]-mn)
                    l.append(z)
        l.sort()
        if l == []:
            print(mx-mn)
        else:
            print(l[0])