for _ in range(int(input())):
    x = 499
    high = 999
    low = 1
    while high >= low:
        print("?",x,x,flush=True)
        ans = int(input())
        if ans == (x+1)**2:
            high = x-1
            x = (high + low)//2
        else:
            low = x+1
            x = (high + low)//2
    print("!",x+1)
    