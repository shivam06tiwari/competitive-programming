for _ in range(int(input())):
    n,k = map(int,input().split())
    l = ["+"]*n
    a = input()
    x = -1
    y = 0
    for ch in a:
        if ch == "0":
            if l[x] == "?":
                l[x] = "-"
                l[x-1] = "?"
                x -= 1
            else:
                l[x] = "-"
                x -= 1
        elif ch == "1":
            if l[y] == "?":
                1[y] = "-"
                l[y+1] = "?"
                y += 1
            else:
                1[y] = "-"
                y += 1
        else:
            if l[x] == "?":
                l[x-1] = "?"
                x -= 1
            else:
                l[x] = "?"
                x -= 1
            if l[y] == "?":
                l[y+1] = "?"
                y += 1
            else:
                1[y] = "-"
                y += 1