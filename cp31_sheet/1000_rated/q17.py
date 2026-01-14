for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(*[0,1])
    else:
        p = len(bin(n)[2:])-1
        if n == 2**p:
            l = [x for x in range(2**(p-1)-1,-1,-1)]
            ll = [x for x in range(2**(p-1),n)]
            l += ll
            print(*l)
            
        else:
            l = [x for x in range(2**p-1,-1,-1)]
            ll = [x for x in range(2**p,n)]
            if n-1-2**p > 0:
                ll.append(n-1-2**p)
                l.remove(n-1-2**p)
            l += ll
            print(*l)
    