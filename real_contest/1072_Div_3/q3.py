for _ in range(int(input())):
    n,k = map(int,input().split())
    c = 0
    f = 0
    if n%2 != 0:
        f = 1
    if n == k:
        print(0)
    elif k>n:
        print(-1)
    else:
        while n != 1:
            if n == k:
                break
            if n%2 != 0:
                if n+1 == k:
                    n += 1
                    break
            if f == 1:
                if n%2 == 0:
                    n += 1
                if n == k:
                    break
            f = 0  
            if n%2 != 0:
                f = 1   
            n //= 2
            c += 1
        if n == k:
            print(c)
        else:
            print(-1)
        
    