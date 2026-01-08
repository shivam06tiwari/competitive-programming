L = []
for _ in range(int(input())):
    n = int(input())
    s = input()
    if "2025" in s:
        if "2026" in s:
            L.append(0)
        else:
            L.append(1)
    else:
        L.append(0)
for ch in L:
    print(ch)