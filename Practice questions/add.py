for _ in range(int(input())):
    n, m = map(int,input().split())
    c1 = 0
    c2 = 0
    mx = 0
    c = 0
    for i in range(n,0,-1):
        print(i)
        for j in range(m):
            print("j",j)
            a = list(map(int,input().split()))
            for k in range(n):
                print("k",k)
                c1 += a[k]*(i*m-k)
                if c1 > mx:
                    z = a.copy()
        c += c1
    print(c)