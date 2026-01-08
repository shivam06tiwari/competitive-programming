for _ in range(int(input())):
    n = int(input())
    s = input()
    c = []
    x = 0
    f = 0
    for i in range(n):
        if s[i] == "." and f == 0:
            x += 1
            f = 1
            if i == n-1:
                c.append(x)
        elif s[i] == "." and f == 1:
            x+=1
            if i == n-1:
                c.append(x)
        else:
            if x!=0:
                c.append(x)
                x = 0
            else:
                continue
    c.sort()
    if c == []:
        print(0)
    elif c[-1] > 2:
        print(2)
    else:
        print(sum(c))


    