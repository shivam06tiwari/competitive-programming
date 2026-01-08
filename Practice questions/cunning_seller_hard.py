L = []
for _ in range(int(input())):
    n, k = map(int,input().split())
    ans = 0
    dif = 0
    l = []
    while n:
        l.append(n%3)
        n = n//3
    if sum(l) > k:
        L.append(-1)
    else:
        for i in range(len(l)-1,-1,-1):
            if i != 0:
                dif = k-sum(l)
                dif = dif//2
                dif = min(dif,l[i])
                l[i] -= dif
                l[i-1] += dif*3
            ans+= l[i]*((3**(i+1))+i*(3**(i-1)))
        L.append(int(ans))
for ch in L:
    print(ch)

