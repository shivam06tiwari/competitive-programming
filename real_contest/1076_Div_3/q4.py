for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse=True)
    c = 0
    mn = 10**18
    sc = 0
    mna = []
    mx = 0
    for i in range(n):
        c += b[i]
        if c > n:
            break
        sc = (i+1)*a[c-1]
        mx = max(mx,sc)
    print(mx)
        
        