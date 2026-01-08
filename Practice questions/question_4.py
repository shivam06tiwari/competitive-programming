L = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    S = 0
    l = []
    mx = 0
    mxn = 0
    for i in range(n):
        S ^= (a[i]^b[i])
    if S == 0:
        L.append("Tie")
        continue
    for i in range(n):
        count = 0
        if max(a[i],b[i]) > mxn:
            if a[i] >= b[i]:
                mxn = a[i]
                while a[i]:
                    a[i] //= 2
                    count += 1
            else:
                mxn = b[i]
                while b[i]:
                    b[i] //= 2
                    count += 1
            if count >= mx:
                mx = count
                if (i+1)%2 == 0:
                    S = 1
                else:
                    S = 2
    if S == 2:
        L.append("Ajisai")
    else:
        L.append("Mai")
for ch in L:
    print(ch)
