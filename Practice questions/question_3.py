L = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    aja = 0
    mai = 0
    
    for i in range(n):
        if (i+1)%2 != 0:
            if a[i] != b[i]:
                aja += 1
        else:
            if a[i] != b[i]:
                mai += 1
    if aja > mai:
        L.append("AJISAI")
    elif mai > aja:
        L.append("MAI")
    else:
        L.append("TIE")
for ch in L:
    print(ch)