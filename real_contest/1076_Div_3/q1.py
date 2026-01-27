for _ in range(int(input())):
    n,s,x = map(int,input().split())
    a = list(map(int,input().split()))
    z = sum(a)
    if z > s:
        print("NO")
    else:
        y = s-z
        if y == 0:
            print("YES")
        elif y%x == 0:
            print("YES")
        else:
            print("NO")