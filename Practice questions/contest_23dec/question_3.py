L = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[1]> 2*a[0]:
        L.append(a[1]-a[0])
    else:
        L.append(a[0])
for ch in L:
    print(ch)