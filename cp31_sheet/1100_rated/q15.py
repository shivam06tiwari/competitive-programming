for i in range(int(input())):
    s = input()
    if s.count("1") == len(s):
        print(len(s)*len(s))
    elif s.count("0") == len(s):
        print(0)
    else:
        mx = 1
        c = 1
        z = s+s
        for i in range(len(z)-1):
            if z[i+1] == z[i] and z[i] == "1":
                c += 1
                if c>mx:
                    mx = c
            else:
                c = 1
        y = mx+1
        print(max(mx,(y//2)*((y+1)//2)))