L = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    S = 0
    for i in range(n):
        S ^= (a[i] ^ b[i])
    if S == 0:
        L.append("TIE")
    else:
        a.sort()
        b.sort()
        
for ch in L:
    print(ch)
