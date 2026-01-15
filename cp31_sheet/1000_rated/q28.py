for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    t = 0
    for ch in s:
        if ch == "(":
            c += 1
        else:
            c -= 1
        if c<0:
            c += 1
            t += 1
    print(t)