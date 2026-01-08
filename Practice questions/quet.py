L = []
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    s = input().strip()
    for ch in s:
        if ch == '8':
            if x > 0:
                x -= 1
            elif x < 0:
                x += 1
            if y > 0:
                y -= 1
            elif y < 0:
                y += 1
        else:
            if abs(x) >= abs(y):
                if x > 0:
                    x -= 1
                elif x < 0:
                    x += 1
            else:
                if y > 0:
                    y -= 1
                elif y < 0:
                    y += 1

    if x == 0 and y == 0:
        L.append("YES")
    else:
        L.append("NO")

for cha in L:
    print(cha)
