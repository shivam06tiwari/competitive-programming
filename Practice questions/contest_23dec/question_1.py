L = []
for _ in range(int(input())):
    a, b = map(int,input().split())
    L.append((a*b)+1)
for ch in L:
    print(ch)