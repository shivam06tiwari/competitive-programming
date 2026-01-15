for _ in range(int(input())):
    n,m = map(int,input().split())
    L = []
    oc = 0
    for i in range(n):
        l = list(map(int,input().split()))
        for j in range(m):
            if l[j] < 0:
                oc += 1
                l[j] = -l[j]
        L.extend(l)
    L.sort()
    if L[0] == 0:
        print(sum(L))
    else:
        if oc%2 == 0:
            print(sum(L))
        else:
            print(sum(L)-2*L[0])
            
        