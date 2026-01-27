for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = sorted(a,reverse = True)
    f = -1
    e = -1
    for i in range(n):
        if a[i] != c[i]:
            f = i
            e = c[i]
            break
    else:
        print(*a)
    if f != -1:
        z = a.index(e)
        while f<z:
            a[f],a[z] = a[z],a[f]
            f += 1
            z -= 1
        print(*a)