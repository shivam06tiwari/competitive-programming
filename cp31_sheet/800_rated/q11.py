n = int(input())
a = list(map(int,input().split()))
mn = abs(a[0])
for ch in a:
    if abs(ch) < mn:
        mn = abs(ch)
print(mn)