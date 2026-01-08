for _ in range(int(input())):
    a,b = input().split()
    dt = {}
    s = []
    for ch in b:
        if ch in dt:
            dt[ch] += 1
        else:
            dt[ch] = 1
    for ch in reversed(a):
        if ch in dt:
            dt[ch] -= 1
            s.append(ch)
    s = str(s)
    s.reverse()
    if s == b:
        print("YES")
    else:
        print("NO")
            