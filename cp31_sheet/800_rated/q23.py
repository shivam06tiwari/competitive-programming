for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if d<b:
        print(-1)
    else:
        s = d-b
        a = a+s
        if a<c:
            print(-1)
        else:
            print(s+(a-c))