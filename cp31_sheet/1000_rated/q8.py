for _ in range(int(input())):
    n = int(input())
    s = input()
    d = {}
    u1 = 0
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            u1 += 1
            d[ch] = 1
    mxx = 0
    u2 = 0
    d2 = {}
    for ch in s:
        d[ch] -= 1
        if d[ch] == 0:
            u1 -= 1
        if ch not in d2:
            u2 += 1
            d2[ch] = 1
        if u1+u2 > mxx:
            mxx = u1+u2
    print(mxx)
        
        
    