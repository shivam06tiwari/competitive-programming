L = []
for _ in range(int(input())):
    m,a,b,c = map(int,input().split())
    s = 0
    ns = 2*m
    if m>=a:
        s += a
        ns -= a
    else:
        s += m
        ns -= m
    if m>=b:
        s += b
        ns -= b
    else:
        s += m
        ns -= m
    if ns>=c:
        s += c
    else:
        s += ns
    L.append(s)
for ch in L:
    print(ch)