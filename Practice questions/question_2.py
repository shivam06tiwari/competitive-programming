L = []
Z = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    sum = 0
    Y = []
    if a.count(-1) == 0:
        for i in range(n-1):
            sum += a[i+1] - a[i]
            if sum < 0:
                L.append(-sum)
            else:
                L.append(sum)
            Y = a.copy()
    elif a[0] == -1 and a[n-1] == -1:
        for i in range(n):
            if i == n-1:
                Y.append(0)
            else:
                if a[i] == -1:
                    a[i] = 0
                    Y.append(0)
                    if a[i+1] == -1:
                        a[i+1] = 0
                    sum += a[i+1] -a[i]
                else:
                    if a[i+1] == -1:
                        a[i+1] = 0
                    sum += a[i+1] -a[i]
                    Y.append(a[i])
    elif a[0] == -1 and a[n-1] != -1:
        for i in range(n-1,-1,-1):
            if a[i] == -1:
                Y.append(0)
                a[i] = 0
                if i != 0:
                    if a[i-1] != -1:
                        sum += a[i] - a[i-1]
                    else:
                        a[i-1] = 0
                        sum += a[i] - a[i-1]
            else:
                if a[i-1] != -1:
                    sum += a[i] - a[i-1]
                else:
                    a[i-1] = 0
                    sum += a[i] - a[i-1]
                Y.append(a[i])
    elif a[0] != -1 and a[n-1] == -1:
        for i in range(n):
            if a[i] == -1:
                if i == n-1:
                    Y.append(0)
                else:
                    a[i] = 0
                    Y.append(0)
                    if i != n-1:
                        if a[i+1] != -1:
                            sum += a[i+1] - a[i]
                        else:
                            a[i+1] = 0
                            sum += a[i+1] - a[i]
            else:
                if a[i+1] != -1:
                    sum += a[i+1] - a[i]
                else:
                    a[i+1] = 0
                    sum += a[i+1] - a[i]
                Y.append(a[i])
    else:
        for i in range(n):
            if a[i] == -1:
                a[i] = 0
                Y.append(0)
                if a[i+1] != -1:
                    sum += a[i+1] - a[i]
                else:
                    a[i+1] = 0
                    sum += a[i+1] - a[i]
            else:
                if i == n-1:
                    Y.append(a[i])
                else:
                    if a[i+1] != -1:
                        sum += a[i+1] - a[i]
                    else:
                        a[i+1] = 0
                        sum += a[i+1] - a[i]
                    Y.append(a[i])
    if sum < 0:
        L.append(-sum)
    else:
        L.append(sum)   
    Z.append(Y)
for i in range(len(L)):
    print(L[i])
    print(*Z[i])
                
                
            