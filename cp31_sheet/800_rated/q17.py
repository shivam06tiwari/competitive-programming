for _ in range(int(input())):
    d = []
    a,b,c = list(map(int,input().split()))
    if c!=1:
        print("YES")
        print(a)
        z = [1]*a
        print(*z)
    else:
        if a%2 == 0:
            if b>1:
                k = a//2
                z = [2]*k
                print("YES")
                print(k)
                print(*z)
            else:
                print("NO")
        else:
            if b>2:
                k = a//2-1
                z = [2]*k
                z.append(3)
                k += 1
                print("YES")
                print(k)
                print(*z)
            else:
                print("NO")