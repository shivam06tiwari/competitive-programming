for i in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    mx = 0
    mn = 0
    s = sum(a)
    if s%x == 0:
        mn = s//x
    else:
        mn = s//x+1
    for ch in a:
        if ch%x == 0:
            mx += ch//x
        else:
            mx += ch//x+1
    print(mn,mx)