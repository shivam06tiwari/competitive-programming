L = []
for _ in range(int(input())):
    n, k = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    c = a.copy()
    x = 0
    for ele in b:
        if len(a) >= ele:
            x += a[-ele]
            del a[-ele:-1]
            a.pop(-1)
        else:
            break
    L.append(sum(c)-x)
for ch in L:
    print(ch)
    