L = []
for _ in range(int(input())):
    s = input()
    c = 0
    for x in s:
        if x == 'Y':
            c += 1
    if c <= 1:
        L.append("YES")
    else:
        L.append("NO")
for ch in L:
    print(ch)