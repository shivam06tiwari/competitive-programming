for _ in range(int(input())):
    n,m,k = map(int,input().split())
    if k == 1 or k == n:
        if m >= (n-3)*2+3:
            print(n)
        else:
            if m >= 1 and m <= 2:
                print(2)
            elif m > 2 and m <= 4:
                print(3)
            else:
                z = (m+3)//2
                print(z)
    else:
        c = 0
        x = k
        y = n-k+1
        if x == y:
            z = x+y -1
            if m >= (z-3)*3//2+2:
                print(z)
            else:
                print((2*m+5)//3)
        elif x!=y:
            c = abs(x-y)
            h = 0
            z = 2*(min(x,y)) -1
            if m >= (z-3)*3//2+2:
                h += z
                m -= (z-3)*3//2+2
            else:
                h += (2*m+5)//3
                m -= (h-3)*3//2+2
            if m >= 1:
                if m >= 2*c:
                    h += c
                else:
                    h += m//2
            print(h)
                
                
      