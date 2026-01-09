for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = [0]*(2*n)
    d = [0]*(2*n)
    cont = 1
    for i in range(n-1):
        if a[i+1] == a[i]:
            cont +=1
        else:
            if c[a[i]-1] < cont:
                c[a[i]-1] = cont
            cont = 1
    if c[a[-1]-1] < cont:
        c[a[-1]-1] = cont
    cont = 1
    for i in range(n-1):
        if b[i+1] == b[i]:
            cont +=1
        else:
            if d[b[i]-1] < cont:
                d[b[i]-1] = cont
            cont = 1
    if d[b[-1]-1] < cont:
        d[b[-1]-1] = cont
    for i in range(2*n):
        c[i] += d[i]
    print(max(c))
            
        