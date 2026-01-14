for _ in range(int(input())):
    n,r,b = map(int,input().split())
    s = ""
    if r == b:
        for i in range(n):
            if i%2 == 0:
                s += "R"
            else:
                s += "B"
    elif r%(b+1) == 0:
        c = r//(b+1)
        s += "R"*c
        for i in range(b):
            s += "B"
            s += "R"*c
    else:
        c = r%(b+1)
        d = r//(b+1)
        z = b+1-c
        while z != 0:
            s += "R"*d
            s += "B"
            z -= 1
        while c != 1:
            s += "R"*(d+1)
            s += "B"
            c -= 1
        s += "R"*(d+1)
    print(s)
            
        