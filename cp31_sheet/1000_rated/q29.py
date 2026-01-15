for _ in range(int(input())):
    a,b = map(int,input().split())
    if a == b:
        print(0)
    elif a>b:
        if a//b == (a+b-1)//b:
            t = 0
            c = a//b
            s = bin(c)[2:]
            if s.count("1") == 1:
                z = s.count("0")
                while z != 0:
                    if z >= 3:
                        z -= 3
                        t += 1
                    elif z>= 2:
                        z -= 2
                        t += 1
                    else:
                        z -= 1
                        t += 1
                print(t)
            else:
                print(-1)
        else:
            print(-1)
    else:
        if b//a == (b+a-1)//a:
            t = 0
            c = b//a
            s = bin(c)[2:]
            if s.count("1") == 1:
                z = s.count("0")
                while z != 0:
                    if z >= 3:
                        z -= 3
                        t += 1
                    elif z>= 2:
                        z -= 2
                        t += 1
                    else:
                        z -= 1
                        t += 1
                print(t)
            else:
                print(-1)
        else:
            print(-1)