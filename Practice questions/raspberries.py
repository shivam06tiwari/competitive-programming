L = []
for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    mul = 1
    flag = 2
    mn = k-(a[0]%k)
    for i in range(n):
        mul *= a[i]
    if mul%k == 0:
        L.append(0)
    elif k == 2:
        L.append(1)
    elif k == 3:
        for i in range(n):
            if mn > k-(a[i]%k):
                mn = k-(a[i]%k)
        L.append(mn)
    elif k == 5:
        for i in range(n):
            if mn > k-(a[i]%k):
                mn = k-(a[i]%k)
        L.append(mn)
    elif k == 4:
        for i in range(n):
            if a[i]%2 == 0:
                flag = 1
                break
            if mn > k-(a[i]%k):
                mn = k-(a[i]%k)
        L.append(min(mn,flag))
for ch in L:
    print(ch)
            
                