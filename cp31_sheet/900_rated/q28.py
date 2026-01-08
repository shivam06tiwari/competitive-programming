for i in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    t = n*k
    c = 0
    if n > 2:
        if n%2 == 0:
            n = n//2+1
        else:
            n = n-n//2
    for i in range(k):
        c += a[t-(i+1)*n]
    print(c)
    
    
    