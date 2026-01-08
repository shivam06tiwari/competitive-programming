for _ in range(int(input())):
    a,b,c = map(int,input().split())
    f = 0
    if a == b and b == c:
        print("YES")
    else:
        d0 = c-a
        if d0%2 == 0:
            d0 //= 2
            b1 = a+d0
            if b1//b == b1/b:
                m0 = b1//b
                if m0 > 0 and f == 0:
                    f = 1
                    print("YES")
        d1 = c-b
        d2 = b-a
        a1 = b-d1
        c1 = b+d2
        if a1//a == a1/a:
            m1 = a1//a
            if m1 > 0 and f == 0:
                f = 1
                print("YES")
        if c1//c == c1/c:
            m2 = c1//c
            if m2 > 0 and f == 0:
                f = 1
                print("YES")
        if f == 0:
            print("NO")
        
    