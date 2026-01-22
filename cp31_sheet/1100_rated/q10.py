for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    z = 0
    for i in range(n):
        if x|a[i] == x:
            z = z|a[i]
        else:
            break
    if z == x:
        print("YES")
    else:
        for i in range(n):
            if x|b[i] == x:
                z |= b[i]
            else:
                break
        if z == x:
            print("YES")
        else:
            for i in range(n):
                if x|c[i] == x:
                    z |= c[i]
                else:
                    break
            if z == x:
                print("YES")
            else:
                print("NO")