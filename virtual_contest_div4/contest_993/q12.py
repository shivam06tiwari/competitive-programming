L = []
for _ in range(int(input())):
    r = input()
    c = r.count("u")
    k = 0
    i = 1
    while i < len(r)-1:
        if r[i] == 'u':
            k += 1
            i += 2
        else:
            i += 1
    L.append(c-k)
for ch in L:
    print(ch)
            