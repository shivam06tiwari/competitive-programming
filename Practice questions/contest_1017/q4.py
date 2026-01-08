L = []
for _ in range(int(input())):
    a = list(input())
    b = list(input())
    x = 0
    y = 0
    da = 0
    db = 0
    f = 0
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            continue
        else:
            da += 1
    for j in range(len(b)-1):
        if b[j] == b[j+1]:
            continue
        else:
            db += 1
    if da == db:
        for k in range(db):
            ca = 1
            cb = 1
            while a[x] == a[x+1]:
                ca += 1
                x += 1
            while b[y] == b[y+1]:
                cb += 1
                y += 1
            x+=1
            y+=1
            if cb >= ca and cb <= 2*ca:
                continue
            else:
                L.append("NO")
                f = 1
                break
        if f == 0:
            L.append("YES")
    else:
        L.append("NO")   
for ch in L:
    print(ch)