for _ in range(int(input())):
    n,k = map(int,input().split())
    c = 0
    mn = n
    mx = n
    if n == k:
        print(0)
    elif k > n:
        print(-1)
    else:
        while mn > k:
            mn //= 2 
            mx = (mx+1)//2
            c += 1
        if k <= mx:
            print(c)
        else:
            print(-1)
    